# Transparencify
This script can transform a regular signature snapshot to a transparent one.

The way Transparencify.py works is that it takes advantage of PIL and walk modules of python in order to:
1. Retrieve the image you want to edit.
2. Process it.
3. Save the processed image.

The Processing phase takes the Image which in our case is the snapshot of a signature (either scanned or a photo in good conditions), scans each pixel, and whenever it comes across a white-ish pixel it changes the value of transparency attribute to zero. hence the resulting image is somewhat a perfect reusable image in different scenarios as you may wish.
