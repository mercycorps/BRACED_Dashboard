from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User


class TolaUser(User):
   class Meta:
      proxy = True

   def __unicode__(self):
        return self.first_name + " " + self.last_name


class Country(models.Model):
    country = models.CharField("Country Name", max_length=255, blank=True)
    code = models.CharField("2 Letter Country Code", max_length=4, blank=True)
    description = models.CharField("Description/Notes", max_length=255, blank=True)
    latitude = models.CharField("Latitude", max_length=255, null=True, blank=True)
    longitude = models.CharField("Longitude", max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('country',)
        verbose_name_plural = "Countries"
        app_label = 'dashboard'

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Country, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.country


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Country'


class Program(models.Model):
    gaitid = models.CharField("GAITID", max_length=255, blank=True, unique=True)
    name = models.CharField("Program Name", max_length=255, blank=True)
    funding_status = models.CharField("Funding Status", max_length=255, blank=True)
    cost_center = models.CharField("Fund Code", max_length=255, blank=True, null=True)
    description = models.CharField("Program Description", max_length=765, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    country = models.ManyToManyField(Country)

    class Meta:
        ordering = ('create_date',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if not 'force_insert' in kwargs:
            kwargs['force_insert'] = False
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Program, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.name


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'edit_date')
    display = 'Program'


class Province(models.Model):
    name = models.CharField("Province Name", max_length=255, blank=True)
    country = models.ForeignKey(Country)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Province, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.name


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'create_date')
    search_fields = ('name','country')
    list_filter = ('create_date','country')
    display = 'Province'


class District(models.Model):
    name = models.CharField("District Name", max_length=255, blank=True)
    province = models.ForeignKey(Province)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(District, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.name


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'create_date')
    search_fields = ('create_date','province')
    list_filter = ('create_date','province')
    display = 'District'


class AdminLevelThree(models.Model):
    name = models.CharField("District Name", max_length=255, blank=True)
    district = models.ForeignKey(District)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(AdminLevelThree, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.name


class AdminLevelThreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'create_date')
    search_fields = ('name','district')
    list_filter = ('create_date','district')
    display = 'Admin Level Three'


class Office(models.Model):
    name = models.CharField("Office Name", max_length=255, blank=True)
    code = models.CharField("Office Code", max_length=255, blank=True)
    province = models.ForeignKey(Province)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Office, self).save()

    #displayed in admin templates
    def __unicode__(self):
        new_name = unicode(self.name) + unicode(" - ") + unicode(self.code)
        return new_name


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'province', 'create_date', 'edit_date')
    search_fields = ('name','province')
    list_filter = ('create_date','province')
    display = 'Office'


class Village(models.Model):
    name = models.CharField("Village Name", max_length=255, blank=True)
    district = models.ForeignKey(District)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Village, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return self.name


class VillageAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'create_date', 'edit_date')
    display = 'Village'


class ProjectType(models.Model):
    name = models.CharField("Type of Activity", max_length=135)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(ProjectType, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'edit_date')
    display = 'Project Type'

class Template(models.Model):
    name = models.CharField("Name of Document", max_length=135)
    documentation_type = models.CharField("Type (File or URL)", max_length=135)
    description = models.CharField(max_length=255)
    file_field = models.FileField(upload_to="uploads", blank=True, null=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Template, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'documentation_type', 'file_field', 'create_date', 'edit_date')
    display = 'Template'



class Documentation(models.Model):
    name = models.CharField("Name of Document", max_length=135, blank=True, null=True)
    url = models.CharField("URL (Link to document or document repository)", blank=True, null=True, max_length=135)
    description = models.CharField(max_length=255, blank=True, null=True)
    template = models.ForeignKey(Template, blank=True, null=True)
    file_field = models.FileField(upload_to="uploads", blank=True, null=True)
    project = models.ForeignKey(ProjectAgreement, blank=True, null=True)
    program = models.ForeignKey(Program, blank=True, null=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

     #onsave add create date or update edit date
    def save(self, *args, **kwargs):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(Documentation, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Documentation"


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'documentation_type', 'file_field', 'program_id', 'create_date', 'edit_date')
    display = 'Documentation'



class MergeMap(models.Model):
    project_agreement = models.ForeignKey(ProjectAgreement, null=True, blank=False)
    project_completion = models.ForeignKey(ProjectComplete, null=True, blank=False)
    from_column = models.CharField(max_length=255, blank=True)
    to_column = models.CharField(max_length=255, blank=True)


class MergeMapAdmin(admin.ModelAdmin):
    list_display = ('project_agreement', 'project_completion', 'from_column', 'to_column')
    display = 'project_agreement'


class ProgramDashboard(models.Model):
    program = models.ForeignKey(Program, null=True, blank=True)
    project_agreement = models.ForeignKey(ProjectAgreement, null=True, blank=True)
    project_completion = models.ForeignKey(ProjectComplete, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('program',)

    #onsave add create date or update edit date
    def save(self):
        if self.create_date == None:
            self.create_date = datetime.now()
        self.edit_date = datetime.now()
        super(ProgramDashboard, self).save()

    #displayed in admin templates
    def __unicode__(self):
        return unicode("Program: %s " % (self.program, self.project_agreement))


class ProgramDashboardAdmin(admin.ModelAdmin):
    list_display = ('program', 'create_date', 'edit_date')
    display = 'Program Dashboard'

# Documentation
class DocumentationApp(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    documentation = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(DocumentationApp, self).save()

    def __unicode__(self):
        return unicode(self.name)


class DocumentationAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'documentation', 'create_date',)
    display = 'DocumentationApp'


# collect feedback from users
class Feedback(models.Model):
    submitter = models.ForeignKey(TolaUser)
    note = models.TextField()
    page = models.CharField(max_length=135)
    severity = models.CharField(max_length=135)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(Feedback, self).save()

    def __unicode__(self):
        return unicode(self.submitter)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('submitter', 'note', 'page', 'severity', 'create_date',)
    display = 'Feedback'


# FAQ
class FAQ(models.Model):
    question = models.TextField(null=True, blank=True)
    answer =  models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('create_date',)

    def save(self):
        if self.create_date is None:
            self.create_date = datetime.now()
        super(FAQ, self).save()

    def __unicode__(self):
        return unicode(self.question)


class FAQAdmin(admin.ModelAdmin):
    list_display = ( 'question', 'answer', 'create_date',)
    display = 'FAQ'