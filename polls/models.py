from __future__ import unicode_literals

from django.db import models
#from django.utils.encoding import python_2_unicode_campatible


 #   @python_2_unicode_campatible
	# class Question(models.Model):
		# """docstring for """

  #  @python_2_unicode_campatible
	# class Choice(models.Model):
		# """docstring for """
	


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# 	def __str__(self):
	# 			return self.question_text

	# def was_published_recently(self):

	# 	return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
	#getting unexpected indentation error here >_
class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete= models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
		# def __str__(self):
		# 	return self.choice_text
	


# Create your models here.
