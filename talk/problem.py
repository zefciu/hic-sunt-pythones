class Person(Versionable):
    title = Field(name = 'title', default = 'Pan/Pani')
    name = Field(name = 'name')
    wage = Numeric(name = 'wage')
