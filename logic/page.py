class Page(object):
    """
    Class used to represent an Page
    """

    def __init__(self, id_page: int, titulo: str = 'titulo', n_pagina: str = "numero de paginas", autor: str= "autor"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_page = id_page
        self._titulo = titulo
        self._n_pagina = n_pagina
        self._autor = autor

    @property
    def id_page(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_page

    @id_page.setter
    def id_page(self, id_page: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_page = id_page

    @property
    def titulo(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._titulo



    @titulo.setter
    def titulo(self, titulo: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._titulo = titulo

    @property
    def n_pagina(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._n_pagina

    @n_pagina.setter
    def n_pagina(self, n_pagina: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._n_pagina = n_pagina

        @property
        def autor(self) -> str:
            """ Returns the name of the person.
              :returns: name of person.
              :rtype: str
            """
            return self._autor

        @autor.setter
        def autor(self, autor: str):
            """ The last name of the person.
            :param last_name: last name of person.
            :type: str
            """
            self._autor = autor

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2},{3})'.format(self.id_page, self.titulo, self.n_paginas,self.autor)


if __name__ == '__main__':

    edwin = Page(id_page=73577376, titulo="Edwin", n_pagina="15", autor="cero")
    print(edwin)