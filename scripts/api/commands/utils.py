import json

import requests

from scripts.models import CommandApproveRequest, Patterns, Parameters


def get_related_objects(relation_name, data, edit=False):
    related_list = [data[k] for k in data if k.startswith(relation_name)]
    to_remove = [k for k in data if k.startswith(relation_name)]
    for k in to_remove:
        if not edit:
            data.pop(k)
    return related_list


def assign_related_objects(command_id, cls, data_list):
    # TODO: delete all before assigning
    cls.objects.filter(command=command_id).delete()
    for element in data_list:
        values = json.loads(element)
        cls.objects.create(**values, command=command_id)


def submit_approval_request(command):
    approval_request = CommandApproveRequest.objects.create(
        command=command,
        status='pending',
    )
    return approval_request


def handle_command_state(request):
    public = request.data.pop('state', ['private'])[0].lower() == 'public'
    request.data['state'] = 'private'
    return public


def _preprocess_edit_request(request):
    script_data = parameters = patterns = None

    if request.data.get('script_dataX.script') is not None:
        script_data = {
            "script_file": request.data.get('script_dataX.script'),
            "dependency_file": request.data.get('script_dataX.requirements'),
            "script_type": request.data.get('script_dataX.scriptType')
        }

    if request.data.get('parametersX[0]') is not None:
        parameters = get_related_objects('parametersX', request.data, True)

    if request.data.get('patternsX[0]') is not None:
        patterns = get_related_objects('patternsX', request.data, True)

    return script_data, parameters, patterns


def _should_rebuild(script_data):
    return script_data is not None


def _should_retrain(parameters, patterns):
    required_for_retrain = [parameters, patterns]
    return any(required_for_retrain)


def _prepare_script_data(script_data):
    return {
        'file': script_data["script_file"],
        'dependency': script_data["dependency_file"],
        'type': script_data["script_type"],
        'name': script_data["script_file"].name
    }


def copy_obj(obj, **kwargs):
    obj.pk = None
    for att, val in kwargs.items():
        setattr(obj, att, val)
    obj.save()
    return obj


def update_nlp_model(command, method='POST'):
    patterns = [{
        'syntax': pattern.syntax,
    }
        for pattern in Patterns.objects.filter(command=command)
    ]

    parameters = [{
        'name': Parameter.name,
        'type': Parameter.type,
        'order': Parameter.order,
    }
        for Parameter in Parameters.objects.filter(command=command)
    ]

    parameters_mapping = {
        'date': 'DATE',
        'location': 'GPE',
        'number': 'number',
    }
    parameters.sort(key=lambda x: x['order'])
    parameters_names = [parameter['name'] for parameter in parameters]
    parameters_types = [parameters_mapping[parameter['type']] for parameter in parameters]
    patterns = [pattern['syntax'] for pattern in patterns]

    serialized_command = {
        "user_id": command.owner.id,
        "user_port": command.owner.port,
        'id': command.id,
        'name': command.name,
        'patterns': patterns,
        'parameters_names': parameters_names,
        'parameters_types': parameters_types
    }

    json_data = json.dumps(serialized_command)
    headers = {'Content-Type': 'application/json'}

    if method == 'POST':
        requests.post('http://localhost:8100/train/', json_data, headers=headers)
    elif method == 'PUT':
        requests.put('http://localhost:8100/train/', json_data, headers=headers)
    elif method == 'DELETE':
        requests.delete('http://localhost:8100/train/', data=json_data, headers=headers)
