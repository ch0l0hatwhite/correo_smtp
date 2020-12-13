print('...######...####...####....#######....##........#######.')
print('.##.....##...##.....##....##.....##...##.......##.....##')
print('.##..........##.....##....##.....##...##.......##.....##')
print('.##..........#########....##.....##...##.......##.....##')
print('.##..........#########....##.....##...##.......##.....##')
print('.##..........##.....##....##.....##...##.......##.....##')
print('.##.....##...##.....##....##.....##...##.......##.....##')
print('...######...####...####....#######....#######...#######.')

Print('')
Print('')
Print('')

import smtplib

corre= smtplib.SMTP_SSL('smtp.gmail.com',465)

correo = input('Tu correo > ')


print('')

print('')


contraseña = input('Tu contraseña  > ')

print('')
print('')

corre.login(correo , contraseña)




mensaje = input('Tu mensaje > ')


print('')
print('')

destinatario = input('destinatario > ')




corre.sendmail
(correo , destinatario , mensaje)

corre.quit()


print('')
print('')



print('Tu mensaje ah sido enviado a ' +
destinatario)


print('')

print('')

