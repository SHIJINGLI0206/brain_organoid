import javabridge
import bioformats


javabridge.start_vm(class_path=bioformats.JARS)
print('TEST JAVA')
javabridge.kill_vm()

