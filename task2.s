	.file	"task2.cpp"
	.option nopic
	.attribute arch, "rv64i2p0_m2p0_a2p0_f2p0_d2p0_c2p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	1
	.globl	_Z7processPi
	.type	_Z7processPi, @function
_Z7processPi:
.LFB0:
	.cfi_startproc
	mv	a5,a0
	addi	a2,a0,20
	li	a0,0
	j	.L4
.L2:
	slliw	a4,a4,1
	addw	a0,a4,a0
.L3:
	addi	a5,a5,4
	beq	a5,a2,.L6
.L4:
	lw	a4,0(a5)
	andi	a3,a4,1
	beq	a3,zero,.L2
	addw	a0,a4,a0
	j	.L3
.L6:
	ret
	.cfi_endproc
.LFE0:
	.size	_Z7processPi, .-_Z7processPi
	.ident	"GCC: () 10.2.0"
