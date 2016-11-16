import vcs, cdms2

vcs_canvas = vcs.init()

cdms_file = cdms2.open("/media/wwy/DATA/wrfoutNoah/wrfout_d02_2016-01-01_00_00_00")

clt_variable = cdms_file("HGT")

vcs_canvas.plot(clt_variable)

vcs_canvas.png("clt.png")