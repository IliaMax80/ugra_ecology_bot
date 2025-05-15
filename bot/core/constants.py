import enum


class UserRole(str, enum.Enum):
    frontend_developer = 'frontend_developer'
    backend_developer = 'backend_developer'
    designer = 'designer'
    dummy = 'dummy'


UserRoleTranslation = {
    UserRole.frontend_developer: 'frontend разработчик',
    UserRole.backend_developer: 'backend разработчик',
    UserRole.designer: 'дизайнер',
    UserRole.dummy: 'на подхвате',
}
