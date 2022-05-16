#SingleInstance Force
SetCapsLockState , AlwaysOff

F14::
Run, C:\Program Files (x86)\Steam\Steam.exe
return

F15::
Run, C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
return

F16::
Run, https://www.youtube.com/watch?v=dQw4w9WgXcQ
return

F17::
Run, taskmgr.exe
return

+F18::Media_Prev
return

F18::Media_Next
return

F19::
Run, explorer.exe
return

F20::
Send, ^c
Sleep 50
Run, http://www.google.com/search?q=%clipboard%
return