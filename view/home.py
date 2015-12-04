from libriarys.baseclass import BaseHandler
from libriarys import project
from libriarys import announcement
from libriarys.admin import brand


class Project():
    pass


class Announcement():
    pass


class HomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        project_list = project.get_all()
        announcement_dict = {}
        for each in project_list:
            announcement_dict[each.id] = announcement.get_announcement_by_project(each.id)
        self.render('home.html', project_list=project_list, announcement_dict =announcement_dict)




