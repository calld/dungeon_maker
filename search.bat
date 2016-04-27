@ECHO OFF
for %%f in (*.py) do (
echo %%f 
findstr ".txt" %%f)

