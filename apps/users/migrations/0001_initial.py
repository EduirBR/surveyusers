# Generated by Django 4.1.3 on 2022-11-28 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='your name is?')),
                ('last_name', models.CharField(max_length=50, verbose_name='and last name?')),
                ('country', models.CharField(choices=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of Congo', 'Democratic Republic of Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Ivory Coast', 'Ivory Coast'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea, North', 'Korea, North'), ('Korea, South', 'Korea, South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Macedonia', 'North Macedonia'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Republic of the Congo', 'Republic of the Congo'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('São Tomé and Príncipe', 'São Tomé and Príncipe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=32, verbose_name='where are you from?')),
                ('biomes', models.CharField(choices=[('forest', 'forest'), ('beach', 'beach'), ('mountains', 'mountains'), ('desert', 'desert')], max_length=50, verbose_name='places u like to travel')),
                ('companies', models.CharField(choices=[('alone', 'alone'), ('family', 'with family'), ('friends', ' with friends')], max_length=50, verbose_name='how do you travel?')),
                ('traveling_frequency', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('often', 'often'), ('monthly', 'monthly'), ('once at year', 'once at year'), ('barely', 'barely')], max_length=20, verbose_name='how often u take a trip?')),
            ],
        ),
    ]
