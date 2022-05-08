import jsonschema
login_result = {'code': 0, 'codeRemark': '成功', 'message': '', 'result': '8d9d45ae25a04a5793aaea79cd5cccfeM01', 'totalCount': None, 'totalPage': None}
login_schema = {"type": ["string", "number", "array"] }
a = jsonschema.validate(instance=login_result, schema=login_schema)
print(a)
