@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

set len=64

set charpool=0123456789abcdefghijklmnopqrstuvw

set len_charpool=16


set gen_str=
for /L %%b IN (1, 1, %len%) do (
  set /A rnd_index=!RANDOM! * %len_charpool% / 32768
  for /F %%i in ('echo %%charpool:~!rnd_index!^,1%%') do set gen_str=!gen_str!%%i
)

REM echo %gen_str%

set KEY=%gen_str%

python D:\CryptoWallet.py
