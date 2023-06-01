# psycopg2-1586

Reproduction of a problem described in https://github.com/jtougas/psycopg2-1586./

# `server-ssl-off.sh`
```
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./listener.py &
[1] 9108
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
[2023-06-01 20:09:55,932][INFO][__main__] len(notifies) == 1
[2023-06-01 20:09:55,933][INFO][__main__] [Notify(65, 'foo', '09:55')]
[2023-06-01 20:09:55,933][INFO][__main__] blocking for 5 seconds
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# [2023-06-01 20:10:00,934][INFO][__main__] continue
[2023-06-01 20:10:00,934][INFO][__main__] len(notifies) == 3
[2023-06-01 20:10:00,934][INFO][__main__] [Notify(66, 'foo', '09:56'), Notify(67, 'foo', '09:57'), Notify(68, 'foo', '09:57')]
[2023-06-01 20:10:00,935][INFO][__main__] blocking for 5 seconds
^C
root@8fb95946cce8:/workspaces/psycopg2-1586# fg
python3 ./listener.py
^CTraceback (most recent call last):
  File "/workspaces/psycopg2-1586/./listener.py", line 28, in <module>
    time.sleep(5)
KeyboardInterrupt
```

# `server-ssl-on.sh`
```
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./listener.py &
[1] 9323
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
[2023-06-01 20:10:45,155][INFO][__main__] len(notifies) == 1
[2023-06-01 20:10:45,155][INFO][__main__] [Notify(56, 'foo', '10:45')]
[2023-06-01 20:10:45,155][INFO][__main__] blocking for 5 seconds
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# python3 ./notifier.py 
root@8fb95946cce8:/workspaces/psycopg2-1586# [2023-06-01 20:10:50,158][INFO][__main__] continue
[2023-06-01 20:10:50,158][INFO][__main__] len(notifies) == 1
[2023-06-01 20:10:50,159][INFO][__main__] [Notify(57, 'foo', '10:45')]
[2023-06-01 20:10:50,159][INFO][__main__] blocking for 5 seconds
[2023-06-01 20:10:55,164][INFO][__main__] continue
[2023-06-01 20:10:55,165][INFO][__main__] len(notifies) == 1
[2023-06-01 20:10:55,165][INFO][__main__] [Notify(58, 'foo', '10:46')]
[2023-06-01 20:10:55,165][INFO][__main__] blocking for 5 seconds
[2023-06-01 20:11:00,170][INFO][__main__] continue
[2023-06-01 20:11:00,170][INFO][__main__] len(notifies) == 1
[2023-06-01 20:11:00,171][INFO][__main__] [Notify(59, 'foo', '10:46')]
[2023-06-01 20:11:00,171][INFO][__main__] blocking for 5 seconds
root@8fb95946cce8:/workspaces/psycopg2-1586# ^C
root@8fb95946cce8:/workspaces/psycopg2-1586# fg
python3 ./listener.py
[2023-06-01 20:11:05,174][INFO][__main__] continue
^CTraceback (most recent call last):
  File "/workspaces/psycopg2-1586/./listener.py", line 17, in <module>
    if select.select([conn],[],[],15) == ([],[],[]):
KeyboardInterrupt
```