# jellyfin-collection-refresher
Fix locked collections and refresh metadata en mass

When the Jellyfin TMDB Box Sets Plugin creates Collections it locks them from edits. If when scraping a collection something goes wrong and the images don't get saved they will never get pulled or saved because of this.
This script is meant to help with that.

**Run the Script:**
python unlock-collections.py

1. Create a backup of your collections - /jellyfin/data/data/collections
2. Run the script and enter the path to your collections folder when asked for input - /jellyfin/data/data/collections
3. Rename the collections folder to - /jellyfin/data/data/collections2
4. In Jellyfin Dashboard->Libraries->Refresh and Scan for New Content on the Collections library
5. Refresh page, make sure no collections are now displayed
6. Rename collections folder back to - /jellyfin/data/data/collection
7. In Jellyfin Dashboard->Libraries->Refresh and Scan for New Content on the Collections library
8. This should now treat all the collections as new, recognize them as unlocked, and pull the data for them.
