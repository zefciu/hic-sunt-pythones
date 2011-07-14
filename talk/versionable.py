class Versionable(object):

    def __init__(self):
        self._current = {}
        self._versions = []
        self._version = None

    def commit(self):
        self._versions.append(self._current.copy())
        self._version = len(self._versions)
        return self._version

    def checkout(self, version):
        if self._version and self._current != self._versions[self._version - 1]:
            raise Exception, 'Uncommited changes exist'
        else:
            self._version = version
            self._current = self._versions[self._version -1].copy()

    def revert(self):
        self._current = self._versions[self._version - 1].copy()
