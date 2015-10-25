##Persistence

Redis provides three persistence options __RDB__, __AOF__ and both. 

__RDB__:  

The RDB option represents point-in-time snapshots of the current dataset. A snapshot is represented as a regular file dump.rdb (by default). Redis regularly dumps its dataset to the file, making it the perfect candidate for backups. Redis can be configured to have it save the dataset every N seconds if there are at least M changes in the dataset, or you can manually call the SAVE or BGSAVE commands. For example, this configuration will make Redis automatically dump the dataset to disk every 60 seconds if at least 1000 keys changed

```
save 60 1000
```
One limitation of this setting of persistence if the possibility of system crashing before it has saved the newest dataset; In that scenario, the data not saved will be lost. __AOF__ settings guards against this scenario 

__AOF__:

The AOF persistence logs every write operation received by the server, that will be played again at server startup, reconstructing the original dataset. Thus, even in an event  of server crash, the data can be recovered. Commands are logged using the same format as the Redis protocol itself, in an append-only fashion. Redis is able to rewrite the log on background when it gets too big. __AOF__ setting can be activated by modifying the __redis.conf__ file with this line

```
appendonly yes
```

by default, the flag is set to no.

The problem with __AOF__ is that the operating system maintains an output buffer and a successful write doesn't necessarily mean that the data gets written (flushed) to the disk immediately. To tell OS to really really write the data to the disk, Redis needs to call the fsync() function right after the write call, which can be slow. That's why Redis provides 3 options:

* __no__: Don't fsync, just let the OS flush the data when it wants. Faster.  
* __always__:  Fsync after every write to the append only log.    
* __everysec__: Fsync only one time every second. 

The everysec option is the default and it's sufficient for most installations.

[Previous](https://github.com/joed7/Redis/blob/master/partitioning.md)  |  [Home](https://github.com/joed7/Redis)  |  [Next](https://github.com/joed7/Redis/blob/master/furtherreading.md)