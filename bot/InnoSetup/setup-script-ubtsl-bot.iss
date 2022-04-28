; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#include "environment.iss"

#define MyAppName "UNICORN Binance Trailing Stop Loss Bot"
#define MyAppVersion "0.5.0"
#define MyAppPublisher "LUCIT Systems and Development"
#define MyAppURL "https://www.lucit.tech"
#define MyAppExeName "ubtsl.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B45308C4-B11C-4831-8B01-83C95C488062}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\LICENSE
InfoBeforeFile=C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\bot\InnoSetup\before_installation.txt
InfoAfterFile=C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\bot\InnoSetup\after_installation.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\bot\dist
OutputBaseFilename=ubtsl_setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ChangesEnvironment=true

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\bot\dist\ubtsl\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "Z:\unicorn-binance-trailing-stop-loss\bot\InnoSetup\ubtsl_config.ini"; DestDir: "{%USERPROFILE}\lucit"; Flags: ignoreversion
Source: "Z:\unicorn-binance-trailing-stop-loss\bot\InnoSetup\ubtsl_profiles.ini"; DestDir: "{%USERPROFILE}\lucit"; Flags: ignoreversion
Source: "C:\Users\Oliver\PycharmProjects\unicorn-binance-trailing-stop-loss\bot\dist\ubtsl\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Tasks]
Name: envPath; Description: "Add to PATH variable"

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
begin
    if (CurStep = ssPostInstall) and IsTaskSelected('envPath')
    then EnvAddPath(ExpandConstant('{app}') +'\bin');
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
    if CurUninstallStep = usPostUninstall
    then EnvRemovePath(ExpandConstant('{app}') +'\bin');
    if CurUninstallStep = usPostUninstall
    then DelTree(ExpandConstant('{app}') +'\bin', True, True, True);
end;

[Run]
Filename: "{cmd}"; Parameters: "/C mkdir ""{app}\bin"""
Filename: "{cmd}"; Parameters: "/C mklink /D ""{app}\bin\ubtsl.exe"" ""{app}\ubtsl.exe"""
Filename: "{%USERPROFILE}\lucit\ubtsl_config.ini"; Description: "Edit the ubtsl_config.ini file"; Flags: postinstall shellexec skipifsilent
Filename: "{%USERPROFILE}\lucit\ubtsl_profiles.ini"; Description: "Edit the ubtsl_profiles.ini file"; Flags: postinstall shellexec skipifsilent
