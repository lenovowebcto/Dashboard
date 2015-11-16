from libriarys.baseclass import BaseHandler
from libriarys import project
from libriarys import announcement
from libriarys.config import brand


class Project():
    pass


class Announcement():
    pass


class HomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        project_list = project.get_all()
        project_id = 1
        announcement_list = []
        try:
            project_id = int(project_id)
            announcement_list = announcement.get_announcement_by_project(project_id)
        except:
            pass
        # for p in project_list:
        #     print(p)
        # for a in announcement_list:
        #     print(a)

        self.render('home.html', project_list=project_list, announcement_list=announcement_list)


