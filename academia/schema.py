import graphene
from graphene_django import DjangoObjectType
from academia.models import Materia, Profesor, Aula


# -------> Profesor
class ProfesorType(DjangoObjectType):
    class Meta:
        model = Profesor
        fields = ("id", "nombre", "correo")


class CreateProfesorMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        correo = graphene.String(required=True)

    profesor = graphene.Field(ProfesorType)

    @classmethod
    def mutate(cls, self, info, nombre, correo):
        profesor = Profesor(nombre=nombre, correo=correo)
        profesor.save()
        return CreateProfesorMutation(profesor=profesor)


class UpdateProfesorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String(required=True)
        correo = graphene.String(required=True)

    profesor = graphene.Field(ProfesorType)

    @classmethod
    def mutate(cls, self, info, id, nombre, correo):
        profesor = Profesor.objects.get(id=id)
        profesor.nombre = nombre
        profesor.correo = correo
        profesor.save()
        return UpdateProfesorMutation(profesor=profesor)


class DeleteProfesorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, self, info, id):
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        return DeleteProfesorMutation(ok=True)


# -------> Materia
class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia
        fields = ("id", "nombre", "descripcion")


class CreateMateriaMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    ok = graphene.Boolean()
    materia = graphene.Field(MateriaType)

    @classmethod
    def mutate(cls, self, info, nombre, descripcion):
        materia = Materia(nombre=nombre, descripcion=descripcion)
        materia.save()
        return CreateMateriaMutation(ok=True, materia=materia)


class UpdateMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    ok = graphene.Boolean()
    materia = graphene.Field(MateriaType)

    @classmethod
    def mutate(cls, self, info, id, nombre, descripcion):
        materia = Materia.objects.get(id=id)
        materia.nombre = nombre
        materia.descripcion = descripcion
        materia.save()
        return UpdateMateriaMutation(ok=True, materia=materia)


class DeleteMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, self, info, id):
        materia = Materia.objects.get(id=id)
        materia.delete()
        return DeleteMateriaMutation(ok=True)


# -------> Aula
class AulaType(DjangoObjectType):
    class Meta:
        model = Aula
        fields = ("id", "fecha", "hora", "tema", "profesor", "materia")


class CreateAulaMutation(graphene.Mutation):
    class Arguments:
        fecha = graphene.String(required=True)
        hora = graphene.String(required=True)
        tema = graphene.String(required=True)
        profesor = graphene.ID(required=True)
        materia = graphene.ID(required=True)

    ok = graphene.Boolean()
    aula = graphene.Field(AulaType)

    @classmethod
    def mutate(cls, self, info, fecha, hora, tema, profesor, materia):
        profesor_instance = Profesor.objects.get(pk=profesor)
        materia_instance = Materia.objects.get(pk=materia)
        aula = Aula(
            fecha=fecha,
            hora=hora,
            tema=tema,
            profesor=profesor_instance,
            materia=materia_instance,
        )
        aula.save()
        return CreateAulaMutation(ok=True, aula=aula)


class UpdateAulaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        fecha = graphene.String(required=True)
        hora = graphene.String(required=True)
        tema = graphene.String(required=True)
        profesor = graphene.ID(required=True)
        materia = graphene.ID(required=True)

    ok = graphene.Boolean()
    aula = graphene.Field(AulaType)

    @classmethod
    def mutate(cls, self, info, id, fecha, hora, tema, profesor, materia):
        profesor_instance = Profesor.objects.get(pk=profesor)
        materia_instance = Materia.objects.get(pk=materia)
        aula = Aula.objects.get(id=id)
        aula.fecha = fecha
        aula.hora = hora
        aula.tema = tema
        aula.profesor = profesor_instance
        aula.materia = materia_instance
        aula.save()
        return UpdateAulaMutation(ok=True, aula=aula)


class DeleteAulaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, self, info, id):
        aula = Aula.objects.get(id=id)
        aula.delete()
        return DeleteAulaMutation(ok=True)


# -------> Querys
class Query(graphene.ObjectType):
    # -------> Profesores
    profesores = graphene.List(ProfesorType)
    profesor = graphene.Field(ProfesorType, id=graphene.ID())

    def resolve_profesores(self, info):
        return Profesor.objects.all()

    def resolve_profesor(self, info, id):
        return Profesor.objects.get(pk=id)

    # -------> Materias
    materias = graphene.List(MateriaType)
    materia = graphene.Field(MateriaType, id=graphene.ID())

    def resolve_materias(self, info):
        return Materia.objects.all()

    def resolve_materia(self, info, id):
        return Materia.objects.get(pk=id)

    # -------> Aulas
    aulas = graphene.List(AulaType)
    aula = graphene.Field(AulaType, id=graphene.ID())

    def resolve_aulas(self, info):
        return Aula.objects.all()

    def resolve_aula(self, info, id):
        return Aula.objects.get(pk=id)


# -------> Mutations
class Mutation(graphene.ObjectType):
    # -------> Profesores
    profesor_create = CreateProfesorMutation.Field()
    profesor_update = UpdateProfesorMutation.Field()
    profesor_delete = DeleteProfesorMutation.Field()

    # -------> Materias
    materia_create = CreateMateriaMutation.Field()
    materia_update = UpdateMateriaMutation.Field()
    materia_delete = DeleteMateriaMutation.Field()

    # -------> Aulas
    aula_create = CreateAulaMutation.Field()
    aula_update = UpdateAulaMutation.Field()
    aula_delete = DeleteAulaMutation.Field()


# -------> schema
schema = graphene.Schema(query=Query, mutation=Mutation)
