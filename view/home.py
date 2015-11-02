from tornado.web import RequestHandler

class Project():
    pass

class Announcement():
    pass
    
    
class HomeHandler(RequestHandler):
    def get(self):
        project1 = Project()
        project1.id = 1
        project1.name = 'ideacentre 300S-08IHH'
        project1.sub_seris = '300S-08IHH'
        project1.cto_number = '90F1CTO1WW'
        project1.brand_name = 'Lenovo DT'
        project1.ad = '2015/9/20'
        project1.eol_date = '2016/3/31'
        project1.planner = 'MingXiuXiang'
        project1.odt_lead = 'Ridge jia'
        project1.mkt_lead = 'Pace chou'
        project1.tpm = 'Ramble'
        project1.mcs_bom = 'Mandy Hao'
        project1.comp_bom = 'Mandy Hao'
        project1.web_cto_pm = 'Andy Wang'
        project1.lois_pm = 'Mandy Miao'
        project1.ial_pm = 'Lanny Li'
        project1.csr_country_scope = 'EMEA'
        project1.web_cto_country_scope = '-'
        project1.csr_name = '90F1CTO1WW'
        project1.por_name = '/'
        project1.updateon = '2015/10/21'
        project1.updateby = 'Andy'
        
        project2 = Project()
        project2.id = 2
        project2.name = 'Montessori AMD 1.5'
        project2.sub_seris = '11e AMD'
        project2.cto_number = '20ABCTO1WW'
        project2.brand_name = 'ThinkPad'
        project2.ad = '2015/3/24'
        project2.eol_date = '2016/3/31'
        project2.planner = 'MingXiuXiang'
        project2.odt_lead = 'Ridge jia'
        project2.mkt_lead = 'Pace chou'
        project2.tpm = 'Ramble'
        project2.mcs_bom = 'Mandy Hao'
        project2.comp_bom = 'Mandy Hao'
        project2.web_cto_pm = 'Andy Wang'
        project2.lois_pm = 'Mandy Miao'
        project2.ial_pm = 'Lanny Li'
        project2.csr_country_scope = 'WW'
        project2.web_cto_country_scope = 'AU/PL'
        project2.csr_name = 'Montessori AMD 1.5'
        project2.por_name = 'MONTESSORI AMD-1.5'
        project2.updateon = '2015/10/21'
        project2.updateby = 'Andy'
        example_list = [project1,project2] 
        
        project_id = self.get_argument('project','')
        
        announcement1 = Announcement()
        announcement1.id = 5019
        announcement1.project_name = "ideacentre 300S-08IHH"
        announcement1.sub_seris = "11e"
        announcement1.launch_type = "New Launch"
        announcement1.web_cto_ad = "03/24/15"
        announcement1.web_cto_tables = "1111"
        announcement1.wet_cto_status = "completed"
        announcement1.lois_eow = "02/10/15"
        announcement1.lois_ad = "03/24/15"
        announcement1.lois_sbb = "100"
        announcement1.lois_mtm = "50"
        announcement1.lois_status ="completed"
        announcement1.ial_eow = "02/10/15"
        announcement1.ial_ad = "03/24/15"
        announcement1.ial_no = "65053"
        announcement1.ial_bpl_no = "BPL0002"
        announcement1.ial_status = "completed"
        announcement1.overall_status = "completed"
        announcement1.note = ""
        announcement1.updateon = '03/10/15'
        announcement1.updateby = 'Andy'
        
        announcement2 = Announcement()
        announcement2.id = 5018
        announcement2.project_name = "ideacentre 300S-08IHH"
        announcement2.sub_seris = "11e"
        announcement2.launch_type = "New Launch"
        announcement2.web_cto_ad = "03/24/15"
        announcement2.web_cto_tables = "2222"
        announcement2.wet_cto_status = "in progress"
        announcement2.lois_eow = "02/10/15"
        announcement2.lois_ad = "03/24/15"
        announcement2.lois_sbb = "100"
        announcement2.lois_mtm = "50"
        announcement2.lois_status ="completed"
        announcement2.ial_eow = "02/10/15"
        announcement2.ial_ad = "03/24/15"
        announcement2.ial_no = "65053"
        announcement2.ial_bpl_no = "BPL0002"
        announcement2.ial_status = "completed"
        announcement2.overall_status = "delay"
        announcement2.note = ""
        announcement2.updateon = '03/10/15'
        announcement2.updateby = 'Andy'
        
        
        announcement3 = Announcement()
        announcement3.id = 5017
        announcement3.project_name = "ideacentre 300S-08IHH"
        announcement3.sub_seris = "11e"
        announcement3.launch_type = "Async"
        announcement3.web_cto_ad = "NA"
        announcement3.web_cto_tables = "NA"
        announcement3.wet_cto_status = "NA"
        announcement3.lois_eow = "02/10/15"
        announcement3.lois_ad = "03/24/15"
        announcement3.lois_sbb = "300"
        announcement3.lois_mtm = "/"
        announcement3.lois_status ="completed"
        announcement3.ial_eow = "02/10/15"
        announcement3.ial_ad = "03/24/15"
        announcement3.ial_no = "65051"
        announcement3.ial_bpl_no = "BPL0003"
        announcement3.ial_status = "in progress"
        announcement3.overall_status = "in progress"
        announcement3.note = "delay risk"
        announcement3.updateon = '03/10/15'
        announcement3.updateby = 'Andy'
        
        announcement4 = Announcement()
        announcement4.id = 5016
        announcement4.project_name = "Montessori AMD 1.5"
        announcement4.sub_seris = "11e"
        announcement4.launch_type = "New Launch"
        announcement4.web_cto_ad = "03/24/15"
        announcement4.web_cto_tables = "1111"
        announcement4.wet_cto_status = "completed"
        announcement4.lois_eow = "02/10/15"
        announcement4.lois_ad = "03/24/15"
        announcement4.lois_sbb = "100"
        announcement4.lois_mtm = "50"
        announcement4.lois_status ="completed"
        announcement4.ial_eow = "02/10/15"
        announcement4.ial_ad = "03/24/15"
        announcement4.ial_no = "65053"
        announcement4.ial_bpl_no = "BPL0002"
        announcement4.ial_status = "completed"
        announcement4.overall_status = "completed"
        announcement4.note = ""
        announcement4.updateon = '03/10/15'
        announcement4.updateby = 'Andy'
        
        announcement5 = Announcement()
        announcement5.id = 5014
        announcement5.project_name = "Montessori AMD 1.5"
        announcement5.sub_seris = "11e"
        announcement5.launch_type = "New Launch"
        announcement5.web_cto_ad = "03/24/15"
        announcement5.web_cto_tables = "2222"
        announcement5.wet_cto_status = "in progress"
        announcement5.lois_eow = "02/10/15"
        announcement5.lois_ad = "03/24/15"
        announcement5.lois_sbb = "100"
        announcement5.lois_mtm = "50"
        announcement5.lois_status ="completed"
        announcement5.ial_eow = "02/10/15"
        announcement5.ial_ad = "03/24/15"
        announcement5.ial_no = "65053"
        announcement5.ial_bpl_no = "BPL0002"
        announcement5.ial_status = "completed"
        announcement5.overall_status = "in progress"
        announcement5.note = ""
        announcement5.updateon = '03/10/15'
        announcement5.updateby = 'Andy'
        
        
        announcement6 = Announcement()
        announcement6.id = 5015
        announcement6.project_name = "Montessori AMD 1.5"
        announcement6.sub_seris = "11e"
        announcement6.launch_type = "Async"
        announcement6.web_cto_ad = "NA"
        announcement6.web_cto_tables = "NA"
        announcement6.wet_cto_status = "NA"
        announcement6.lois_eow = "02/10/15"
        announcement6.lois_ad = "03/24/15"
        announcement6.lois_sbb = "300"
        announcement6.lois_mtm = "/"
        announcement6.lois_status ="completed"
        announcement6.ial_eow = "02/10/15"
        announcement6.ial_ad = "03/24/15"
        announcement6.ial_no = "65051"
        announcement6.ial_bpl_no = "BPL0003"
        announcement6.ial_status = "in progress"
        announcement6.overall_status = "in progress"
        announcement6.note = "delay risk"
        announcement6.updateon = '03/10/15'
        announcement6.updateby = 'Andy'
        status = {
        'completed':'success',
        'in porgress':'info',
        'delay':'danger'
        }
        for ann in filter(lambda x:x.startswith('announcement'),locals().keys()):
            if eval(ann).overall_status == "completed":
                eval(ann).status_class = 'success'
            elif eval(ann).overall_status == "in progress":
                eval(ann).status_class = 'info'
            else:
                eval(ann).status_class = 'error'
        example_announce_list = []
        try:
            project_id = int(project_id)
            example_announce_list = {1:[announcement1,announcement2,announcement3],2:[announcement4,announcement5,announcement6]}.get(project_id)
        except:
            pass
        self.render('home.html',project_list = example_list,announcement_list = example_announce_list)


