from django.db import models
from django.utils import timezone
#FORKLIFT PROPERY
class ActuatorLog(models.Model):

	Machine1 = '1'
	Machine2 = '2'
	Maquinas = [
	(Machine1, 'Triangle Polybag B'),
	(Machine2, 'Triangle Polybag RJ'),
    ]

	Assy1 = '1'
	Assy2 = '2'
	Assy3 = '3'
	Assy4 = '4'
	Assy5 = '5'
	Assys = [
	(Assy1, 'Accumulator'),
	(Assy2, 'Scale'),
	(Assy3, 'Front Holding Chamber'),
	(Assy4, 'Rear Holding Chamber'),
	(Assy5, 'Holding Chamber Arm'),

    ]

	Unit1 = '1'
	Unit2 = '2'
	Unit3 = '3'
	Unit4 = '4'
	Unit5 = '5'
	Unit6 = '6'
	Unit7 = '7'
	Unit8 = '8'
	Unit9 = '9'
	Units = [
	(Unit1, 'Unit 1'),
	(Unit2, 'Unit 2'),
	(Unit3, 'Unit 3'),
	(Unit4, 'Unit 4'),
	(Unit5, 'Unit 5'),
	(Unit6, 'Unit 6'),
	(Unit7, 'Unit 7'),
	(Unit8, 'Unit 8'),
	(Unit9, 'Unit 9'),
   	]

	id = models.AutoField(primary_key=True)
	fecha = models.DateTimeField(default=timezone.now)
	poly = models.CharField(max_length=2, choices=Maquinas, default=Machine1)
	assy = models.CharField(max_length=2, choices=Assys, default=Assy1)
	unit = models.CharField(max_length=2, choices=Units, default=Unit1)
	def __str__(self):
		return self.poly