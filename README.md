# aws lambda reverse shell

On a machine with a public IP run netcat, eg: `netcat -l 20300`
Modify `event.json` with your IP and port
Deploy the lambda `serverless deploy`
Invoke `make invoke`

The netcat session will now have a shell:
```
sh-4.2$ df
df
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/root        6127168 3714232   2396552  61% /
/dev/vdb         1965904   45356   1904164   3% /dev
/dev/loop0        538424     440    526148   1% /tmp
/dev/loop1           128     128         0 100% /var/task
```


Sourced from https://epsagon.com/blog/lambda-internals-exploring-aws-lambda/

