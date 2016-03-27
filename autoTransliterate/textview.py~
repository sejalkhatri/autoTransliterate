import pygtk
import gtk
def on_key_press_event(widget, event):
    keyname = gtk.gdk.keyval_name(event.keyval)
    print keyname
'''
    if keyname == "space":
        return True
    return False
'''
if __name__ == '__main__':
    w  = gtk.Window()
    w.connect('destroy',lambda x: gtk.main_quit())
    image=gtk.Image()
    image.set_from_file("text.jpeg")
    tv = gtk.TextView()
    tv.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse('black'))
    tv.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse('white'))
    buffr = gtk.TextBuffer()
    buffr.set_text("WHATEVER TEXT")
    tv.connect('key_press_event', on_key_press_event)
    tv.set_buffer(buffr)
    w.add(tv)
    w.show_all()
    gtk.main()

