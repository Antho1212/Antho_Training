.text
maina:
    lw $s0, 0($s3)      # charge sur a 
mainb:
    lw $t0, 4($s3)      # charge
    lw $t1, 8($s4)
    add $s1, $t0, $t1   # add

mainc:
    addi $t0, $s2, -4
    add $t0, $t0, $s1
    sw $t0, 20($s4)

maind:
    lw $t0, 16($s3)
    bne $t0; $zero, ELSE
    sll $t0, $s1, 2                #partie a revoir
    add $t0, $t0, $s3
    lw $s0, 0($t0)
    j EXIT_IF
ELSE :
    sll $t0, $s2, 2
    add $t0, $t0, $s4
    lw $s0, 0($t0)
EXIT_IF :
