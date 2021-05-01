ifeq ($(PREFIX),)
    PREFIX := /usr/local
endif

DESKTOP_SWITCHER:=desktop-image-switcher

install: $(DESKTOP_SWITCHER)
	install -d $(DESTDIR)$(PREFIX)/bin
	install -m 755 $(DESKTOP_SWITCHER) $(DESTDIR)$(PREFIX)/bin

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/$(DESKTOP_SWITCHER)
