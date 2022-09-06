import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()  # команда hello, return тип данных String

    # обработчик команды
    def resolve_hello(self, info):  # info - информация о схеме вызова
        return 'world!'


schema = graphene.Schema(query=Query)

# http://127.0.0.1:8000/graphql/
# вид запроса
# {
#     hello
# }
# ответ
# {
#   "data": {
#     "hello": "world!"
#   }
# }