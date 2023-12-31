# Generated by Django 4.1.2 on 2023-05-23 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profileutility', '0004_rename_cust_id_paymentrequest_channel_and_more'),
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Error', 'Error'), ('Declined', 'Declined')], default='Pending', max_length=50)),
                ('payment_id', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('cust_id_or_reg_no', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('itemlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemlist')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profile')),
            ],
            options={
                'verbose_name': 'App Bookings',
                'verbose_name_plural': 'App Bookings',
            },
        ),
        migrations.CreateModel(
            name='UsedCarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=250, null=True)),
                ('model', models.CharField(blank=True, max_length=250, null=True)),
                ('transmission', models.CharField(blank=True, max_length=250, null=True)),
                ('fuel', models.CharField(blank=True, max_length=250, null=True)),
                ('year', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('cust_id_or_reg_no', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('kms_driven_starting', models.CharField(blank=True, max_length=250, null=True)),
                ('kms_driven_ending', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('lat', models.CharField(blank=True, max_length=250, null=True)),
                ('long', models.CharField(blank=True, max_length=250, null=True)),
                ('enquire_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled', models.DateTimeField(auto_now=True, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('referred_by', models.CharField(blank=True, max_length=255, null=True)),
                ('booking_status', models.CharField(choices=[('Enquired', 'Enquired'), ('Contacted', 'Contacted'), ('Booked', 'Booked'), ('Deliverred', 'Deliverred'), ('Cancelled', 'Cancelled'), ('Car not available', 'Car not available')], default='Enquired', max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profileaddress')),
                ('booking_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.appbooking')),
                ('item_desc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemdescription')),
                ('itemlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemlist')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profile')),
            ],
            options={
                'verbose_name': 'UsedCar Booking',
                'verbose_name_plural': 'UsedCar Booking',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('cust_id_or_reg_no', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('outlet', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('varient', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('pickup_slot', models.DateTimeField(auto_now=True)),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('referred_id', models.CharField(blank=True, max_length=255, null=True)),
                ('deliverred_time', models.DateTimeField(blank=True, null=True)),
                ('booking_status', models.CharField(choices=[('Booked', 'Booked'), ('Contacted', 'Contacted'), ('Picked Up', 'Picked Up'), ('Deliverred', 'Deliverred'), ('Cancelled', 'Cancelled')], default='Booked', max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profileaddress')),
                ('booking_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.appbooking')),
                ('item_desc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemdescription')),
                ('itemlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemlist')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profile')),
            ],
            options={
                'verbose_name': 'Service Booking',
                'verbose_name_plural': 'Service Booking',
            },
        ),
        migrations.CreateModel(
            name='NewCarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=250, null=True)),
                ('cust_id_or_reg_no', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('outlets', models.CharField(blank=True, max_length=250, null=True)),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('referred_by', models.CharField(blank=True, max_length=255, null=True)),
                ('booking_status', models.CharField(choices=[('Booked', 'Booked'), ('Retail', 'Retail'), ('RetailCancel', 'RetailCancel'), ('Deliverred', 'Deliverred')], default='Booked', max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profileaddress')),
                ('booking_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.appbooking')),
                ('item_description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='showcase.itemdescription')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profileutility.profile')),
            ],
            options={
                'verbose_name': 'NewCar Booking',
                'verbose_name_plural': 'NewCar Booking',
            },
        ),
    ]
