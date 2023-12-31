# Generated by Django 4.1.2 on 2023-06-01 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poststreams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Streamscomments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, null=True)),
                ('poststream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streamcom', to='poststreams.poststreams')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststreams.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Repliedcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_comment', models.CharField(max_length=255, null=True)),
                ('streamscomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streamrlpcom', to='poststreams.streamscomments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststreams.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Poststreamimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, default=0, null=True, upload_to='store/backgroundimage')),
                ('emoji', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/streamimages')),
                ('poststream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stream', to='poststreams.poststreams')),
            ],
        ),
        migrations.CreateModel(
            name='Streamslikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poststream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streamlike', to='poststreams.poststreams')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststreams.profile')),
            ],
            options={
                'unique_together': {('poststream', 'user')},
            },
        ),
        migrations.CreateModel(
            name='StreamscommentsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streamscommentlike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streamscommentslike', to='poststreams.streamscomments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststreams.profile')),
            ],
            options={
                'unique_together': {('streamscommentlike', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Repliedcommentlikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repliedcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repliedcommentlike', to='poststreams.repliedcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststreams.profile')),
            ],
            options={
                'unique_together': {('repliedcomment', 'user')},
            },
        ),
    ]
