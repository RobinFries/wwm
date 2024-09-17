Aufgrund von Schwerem Unwetter wurde unser Schultag in Remote gelegt. Als Arbeitsauftrag haben wir eine Aufgabe bekommen. Es sollte ein "Wer-wird-Millionär" ähnliches Quiz mit GUI erstellen.

Ich hab zubeginn die Aufgabenstellung einmal bei ChatGPT reingeworfen und geschaut wie er es machen würde. Das Ergbnis war "Von weit weg schön, aber weit weg von schön". Aber es funktionierte.
ChatGPT hat hierzu Python mit TKinter verwendet. Das ist auch der Grund, warum ich dabei geblieben bin. Ich kenne Python nicht besonders und wollte es mal ausprobieren. Ich bin bei
Programmiersprachen als Datenbankentwickler eher bei proprietären Sprachen wie C/AL zuhause, aber man will sich ja weiter bilden.

CleanCode wir hier als Verwörrungsmythos angesehen. Der Quellcode ist wie das erste Ergebnis von ChatGPT, aber meine herangehensweise beschränken sich auf 3 Phasen:
  1.  Coden bis es funktioniert
  2.  Schön machen
  3.  Fixen, weil es nicht mehr funktioniert

final v1:
Der Code funktionert aus einer IDE wie VSC ohne Probleme. Es gibt 6 textdateinen im bestimmten Format, die zufällig eingelesen werden. Eine Automatische Erkennung gibt es nicht. In der Entwicklung
hatte ich versucht, die verschiedenen dateien in Unterordner zu verpacken, um zumindest die Dateistruktur sauber zu haben. Auch ein Anfragen der Anzahl an Dateien im Ordner könnte so eine externe
Erweiterung möglich machen, ohne den Code anpassen zu müssen. Es gab aber einige Probleme, da ein "\" in Python doch recht viele Probleme machen, auch wenn es nur im String sein soll. Dies endete
darin, dass ich den Code zu vermurkst hatte, dass der entstandene .exe (mit PYInstaller) lauffähig war, aber aus der IDE nicht mehr. WTF?

Ziel könnten sein:
  -  Dateistruktur in den Griff bekommen
  -  Vollbildmodus
  -  Umbau auf CustomTKinter
  -  Soweit anpassen, dass eine .exe erstellt werden kann

Ich glaub aber, dass ich nicht weiter mache, da die Aufgabenstellung mit der Version 100% erfüllt ist. Wer ein gutes WWM haben will, da gibts auf Git ein gutes Repo mit vernünfiter Datenbankverbindung.

Sollte sich eine arme Seele dieses Repo antun, ist das mindeste, was ich machen kann, alles frei zu Verfügung zu stellen. Have fun and God bless you.
