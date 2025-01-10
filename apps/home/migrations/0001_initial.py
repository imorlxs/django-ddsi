# Generated by Django 3.2.6 on 2025-01-10 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campana',
            fields=[
                ('id_campana', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_campana', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('pendiente', 'Pendiente'), ('finalizada', 'Finalizada')], max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('DNIEmpleado', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombreEmpleado', models.CharField(max_length=20)),
                ('apellidosEmpleado', models.CharField(max_length=40)),
                ('cargo', models.CharField(max_length=20)),
                ('telefonoEmpleado', models.CharField(max_length=20)),
                ('emailEmpleado', models.CharField(max_length=40)),
                ('direccionEmpleado', models.CharField(max_length=40)),
                ('fecha_nacEmpleado', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id_gasto', models.AutoField(primary_key=True, serialize=False)),
                ('monto_gasto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id_ingreso', models.AutoField(primary_key=True, serialize=False)),
                ('monto_ingreso', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ID_producto', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=24)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tallas', models.CharField(max_length=60)),
                ('proveedor', models.CharField(max_length=24)),
                ('avisar_restock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('DNISocio', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombreSocio', models.CharField(max_length=24)),
                ('apellidosSocio', models.CharField(max_length=24)),
                ('emailSocio', models.CharField(max_length=40)),
                ('telefonoSocio', models.CharField(max_length=9)),
                ('direccionSocio', models.CharField(max_length=40)),
                ('fecha_nacSocio', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('dnisocio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.socio')),
                ('id_ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ingreso')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ordena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_gasto', models.DateField()),
                ('hora_gasto', models.DateTimeField()),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.empleado')),
                ('id_gasto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.gasto')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.producto')),
            ],
            options={
                'unique_together': {('id_producto', 'id_gasto')},
            },
        ),
        migrations.CreateModel(
            name='Genera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_genera', models.DateField()),
                ('id_campana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.campana')),
                ('id_gasto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.gasto')),
            ],
            options={
                'unique_together': {('id_campana', 'id_gasto')},
            },
        ),
    ]
