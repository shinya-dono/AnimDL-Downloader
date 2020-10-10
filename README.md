# animdl.ir Downloader
thanks to our awesome website animdl.ir we iranians can now download animes and enjoy
<br>
here is a helper script that allows you to download animes without doing too much
<br>

## How to Use
* just visit the website, copy the id at the end of url (e.x. : https://anime-list6.gq/anime/7403 gives us 7403 as the id)
* run the app using CMD with python: ``` python3 CLI.py {id}``` (without {})
* select desired quality (just enter the number)
* enter your directory to save downloaded files

## switches 

there are some useful switches for your ease 
* ``-m or --max-quality`` automatically selects the latest quality, skipping the quality selection
* `` -s or --season `` changing the number of saving directory from ``` /your/anime/path/Season 1``` to what ever you set
* ``-e or --episodes`` specifies episodes to download (script downloads all episodes by default ) 


## TO DO
* add GUI (in progress)
* search and select by name
* custom naming and subtitle downloading

## disclaimer 
im just automating my anime downloading process, i don't own neither the animes nor the website

## contribution 

feel free to send your pull request, DRY code and comment if necessary