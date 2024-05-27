import os
import mimetypes


def attach_file(msg, filepath):
    filename = os.path.basename(filepath)
    mimetype, _ = mimetypes.guess_type(filepath)
    if mimetype is None:
        mimetype = "application/octet-stream"
    maintype, subtype = mimetype.split("/", 1)

    with open(filepath, "rb") as fp:
        msg.add_attachment(
            fp.read(), maintype=maintype, subtype=subtype, filename=filename
        )
