import cherrypy, json, os
from credit_scoring import CreditScoring
from crif_reader import CrifReader

class CreditScoringServer(object):

    def __init__(self):
        self.__credit_scoring = CreditScoring()
        self.__crif_reader = CrifReader()

    @cherrypy.expose
    @cherrypy.tools.params()
    def credit_score(self, json_data: str):
        try:
            cherrypy.response.headers['Access-Control-Allow-Origin'] = "*"
            return json.dumps({"credit_score": self.__credit_scoring.score(json.loads(json_data))})
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e)) 

    @cherrypy.expose
    def upload(self, ufile):
        upload_path = '/home/ubuntu/credit_scoring/backend/files/'
        upload_filename = 'tmp.pdf'
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        return json.dumps(self.__crif_reader.read(upload_file))


cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 8090
cherrypy.quickstart(CreditScoringServer())
