from django.db import models
from django.db.models.signals import post_save
from chosen import forms as chosenforms
from django import forms
from taggit.models import Tag
from taggit.models import TagBase
from taggit.managers import TaggableManager

class TeachSkills(models.Model):
    skills = TaggableManager()

class LearnSkills(models.Model):
    skills = TaggableManager()

# class FoodManager(models.Manager):
#     def create(self, name):
#         new_user = Food()
#         new_user.name = name
#         new_user.teach = TeachSkills()
#         new_user.teach.save()
#         new_user.learn = LearnSkills()
#         new_user.learn.save()
#         new_user.save()
#         return new_user

class Food(models.Model):
    # ... fields here
    # objects = FoodManager()
    name = models.CharField(max_length=20, blank=True)
    
    # create method must populate these with new teach/skill models
    teach = models.ForeignKey(TeachSkills, null=True)
    learn = models.ForeignKey(LearnSkills, null=True)

    def save_skill_teach(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.teach.skills.add(tag_skill)
        self.teach.skills.add(tag)
        return tag + " tag saved."   

    def save_skill_learn(self, tag, level):
        tag_skill = "%s %s" %(tag, level)
        tag = "%s" %(tag)
        self.learn.skills.add(tag_skill)
        self.learn.skills.add(tag)
        return tag + " tag saved."   

    def get_skill_teach(self):
        return self.teach.skills.all()

    def get_skill_learn(self):
        return self.learn.skills.all()

def create_skill_association(sender, instance, created, **kwargs):
    if created:
        instance.teach = TeachSkills()
        instance.teach.save()
        instance.learn = LearnSkills()
        instance.learn.save()

post_save.connect(create_skill_association, sender=Food)
    
class TagUserFind(models.Model):

    def get_tag_user(self, tag):
        return Food.objects.filter(tags__name__in=tag).distinct()

class Skills(models.Model):

    def get_available_tags(self):
        return ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Javascript", "Node.js", "Angular", "Backbone", "Scala", "PHP", "Java", "HTML5", "CSS3", "Jquery"]

    def get_available_skill_levels(self):
        return ["No Experience", "Beginner", "Intermediate", "Expert"]

    def generate_tags(self):
        tags = self.get_available_tags()
        skills = self.get_available_skill_levels()

# Model with a character field that will fit all of the skills imaginable
# Base tags to select from
# For use with chosen
# 

