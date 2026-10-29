/* hide_menubar_shim.dylib - keep the menu bar out of reach while Fallout4.exe is active.
 * winemac.drv releases the mouse when any menu starts tracking (cocoa_app.m:
 * NSMenuDidBeginTrackingNotification -> releaseMouseCapture). A click on the top
 * row of the screen opens the auto-hidden menu bar, so the game loses the mouse.
 * NSApplicationPresentationHideMenuBar removes the bar entirely (no reveal on hover).
 * Only acts in the process whose name contains HIDE_MENUBAR_PROC (default Fallout4.exe).
 * HIDE_MENUBAR_DEBUG=1 logs to stderr. */
#import <AppKit/AppKit.h>
#include <crt_externs.h>
#include <stdlib.h>
#include <string.h>

static BOOL is_target(void)
{
    const char *want = getenv("HIDE_MENUBAR_PROC");
    const char *argv0 = *_NSGetArgv() ? (*_NSGetArgv())[0] : NULL;
    const char *name = [[[NSProcessInfo processInfo] processName] UTF8String];
    if (!want || !*want) want = "Fallout4.exe";
    return (argv0 && strcasestr(argv0, want)) || (name && strcasestr(name, want));
}

static void apply(NSNotification *note)
{
    if (!is_target()) return;
    NSApplicationPresentationOptions want = NSApplicationPresentationHideDock |
                                            NSApplicationPresentationHideMenuBar;
    NSApplicationPresentationOptions cur = [NSApp presentationOptions];
    /* the Auto-hide flags cannot be combined with their Hide counterparts */
    cur &= ~(NSApplicationPresentationAutoHideDock | NSApplicationPresentationAutoHideMenuBar);
    if (([NSApp presentationOptions] & want) != want)
        [NSApp setPresentationOptions:cur | want];
    if (getenv("HIDE_MENUBAR_DEBUG"))
        fprintf(stderr, "hide_menubar_shim: %s on %s options=0x%lx\n", (*_NSGetArgv())[0],
                [[note name] UTF8String], (unsigned long)[NSApp presentationOptions]);
}

/* Becoming active is the normal trigger; a window becoming key covers launches
 * where the activation notification came before this observer existed. */
__attribute__((constructor)) static void init(void)
{
    NSNotificationCenter *nc = [NSNotificationCenter defaultCenter];
    for (NSString *name in @[NSApplicationDidBecomeActiveNotification, NSWindowDidBecomeKeyNotification])
        [nc addObserverForName:name object:nil queue:nil usingBlock:^(NSNotification *note) { apply(note); }];
}
