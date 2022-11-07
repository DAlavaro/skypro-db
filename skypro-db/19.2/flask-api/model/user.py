from flask_restx import Resource


@user_ns.route("/<int:id_>")
class UserView(Resource):
    @admin_required
    def delete(selfself, id_):
        user_service.delete(id_)

        return "", 204
