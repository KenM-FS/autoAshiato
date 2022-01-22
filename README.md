# autoAshiato
Automatically draw lots of あしあと抽選ポイント(Ashiato Chusen Point) in honto

## Initial setting
Make json file for personal information
``` secret.json 
{
	"MAIL_ADDRESS":"yourMailAddress@example.com",
	"HONTO_PASS":"PasswordForHonto",
	"SMTP_PASS":"SMTPPasswordForGmail"
}
```

Change path of secret.json and geckodriver respectively in the environment
- autoAshiato.py
	- line 10: secret.json
	- line 16: geckodriver
- mailerAshiato.py
	- line  8: secret.json

## Set crontab
19:00 UTC is 04:00 JST when Ashiato Chusen Point lottery is updated
```
0 19 * * * /usr/bin/python3 /home/ken/honto/autoAshiato.py >> /home/ken/honto/ashiato.log 2>&1
```

