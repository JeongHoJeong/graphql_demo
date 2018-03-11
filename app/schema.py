import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from app.models import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    """
    query {
        users {
            id
        }
    }
    """
    users = graphene.List(User)

    """
    Since `all_users` is a field defined by SQLAlchemyConnectionField,
    this field simply returns all of the users.
    Also it needs relay.Node interface.

    query {
        allUsers {
            edges {
                node {
                    id
                }
            }
        }
    }
    """
    all_users = SQLAlchemyConnectionField(User)

    def resolve_users(self, info):
        """ Corresponds to `users` field. """
        query = User.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query, types=[User])
