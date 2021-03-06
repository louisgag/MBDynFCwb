import FreeCAD as App
import MBDyn_objects.MBDynJoints
import MBDyn_objects.model_so

def writeVect(vector):
   if vector.x == 0 and vector.y == 0 and vector.z == 0:
      return "null"
   else:
      return "{}, {}, {}".format(vector.x, vector.y, vector.z)

# matrix is a list of 3 FreeCAD vectors
def writeMatrix(matrix_type, matrix):
    '''writes matrix to MBDyn input file'''
    line_end = ""
    matrix_line = ""
    rowcount = 0
    colcount = 0
    if matrix_type == "eye" or matrix_type == "null":
       matrix_line = "{}".format(matrix_type)
    elif matrix_type == "matr":

        matrix_line = "{}".format(matrix_type)
        for j in matrix:
            for i in [j.x, j.y, j.z]:
                line_end = line_end + ", " + "{}".format(i)
        matrix_line = matrix_line + line_end
    elif matrix_type == "sym":
        matrix_line = "{}".format(matrix_type)
        for j in matrix:
            rowcount = rowcount +1
            colcount = 0
            for i in [j.x, j.y, j.z]:
                colcount = colcount + 1
                if colcount >= rowcount:

                    line_end = line_end + ", " + "{}".format(i)
        matrix_line = matrix_line + line_end
    elif matrix_type == "skew":
        matrix_line = "{}".format(matrix_type)
        for j in matrix:
            rowcount = rowcount +1
            colcount = 0
            for i in [j.x, j.y, j.z]:
                colcount = colcount + 1
                if colcount >= rowcount:
                    line_end = line_end + ", " + "{}".format(i)
        matrix_line = matrix_line + line_end
    elif matrix_type == "diag":
        matrix_line = "{}".format(matrix_type)
        for j in matrix:
            rowcount = rowcount +1
            colcount = 0
            for i in [j.x, j.y, j.z]:
                colcount = colcount + 1
                App.Console.PrintMessage("row= {}, col= {}".format(rowcount, colcount))
                if colcount == rowcount:
                    App.Console.PrintMessage("row= {}, col= {}".format(rowcount, colcount))
                    line_end = line_end + ", " + "{}".format(i)
        matrix_line = matrix_line + line_end
    return matrix_line

# Orientationmatrix passed is a list of three FreeCAD vectors even if only 2 are used
def writeOrientationMatrix(description, Orientationmatrix):
    '''writes orientation matrix to MBDyn input file'''
#    teststr = "MBDyn {} description".format(description)
#    App.Console.PrintMessage("dscr" + str(description))
    line_end = ""
    matrix_line = ""
    if description == "eye" or description == "null":
        matrix_line = "{}".format(description)
    elif description == "matr":
        rowcount = 0
        colcount = 0

        matrix_line = "{}".format(description)
        for j in Orientationmatrix:
            for i in [j.x, j.y, j.z]:
                line_end = line_end + ", " + "{}".format(i)
        matrix_line = matrix_line + line_end
     # description xy, xz, yz are for OM with 2 vectors
    elif description == "xy":
        matrix_line = "1, {}, {}, {},  2, {}, {}, {}".format(Orientationmatrix[0][0], Orientationmatrix[0][1], Orientationmatrix[0][2], Orientationmatrix[1][0], Orientationmatrix[1][1], Orientationmatrix[1][2])
    elif description == "xz":
        matrix_line = "1, {}, {}, {},  3, {}, {}, {}".format(Orientationmatrix[0][0], Orientationmatrix[0][1], Orientationmatrix[0][2], Orientationmatrix[2][0], Orientationmatrix[2][1], Orientationmatrix[2][2])
    elif description == "yz":
        matrix_line = "2, {}, {}, {},  3, {}, {}, {}".format(Orientationmatrix[1][0], Orientationmatrix[1][1], Orientationmatrix[1][2], Orientationmatrix[2][0], Orientationmatrix[2][1], Orientationmatrix[2][2])
    else:
        matrix_line = "{}, {}, {}, {}".format(description, Orientationmatrix[0][0], Orientationmatrix[0][1], Orientationmatrix[0][2] )
    return matrix_line

def writeInputFile(name_of_file):
    ''' writes MBDyn input file'''
    with open(name_of_file, "w") as f:
        if hasattr(App.ActiveDocument, "initial_values"):
            f.write("begin: data;\n")
            f.write("        problem: initial value;\n")
            f.write("end: data;\n\n")

            f.write("begin: initial value;\n")
            f.write(App.ActiveDocument.initial_values.Proxy.writeInitialValue())
#            if hasattr(App.ActiveDocument, "integration_method"):
#                f.write(App.ActiveDocument.integration_method.Proxy.writeMethod())
            f.write("end: initial value;\n\n")

            f.write("begin: control data;\n")
            if len(App.ActiveDocument.Nodes.getSubObjects()) != 0:
                f.write("        structural nodes: {};\n".format(len(App.ActiveDocument.Nodes.getSubObjects())))
            if len(App.ActiveDocument.Joints.getSubObjects()) != 0:
                f.write("        joints: {};\n".format(len(App.ActiveDocument.Joints.getSubObjects())))
            if len(App.ActiveDocument.Bodies.getSubObjects()) != 0:
                f.write("        rigid bodies: {};\n".format(len(App.ActiveDocument.Bodies.getSubObjects())))
            if len(App.ActiveDocument.Forces.getSubObjects()) != 0:
                f.write("        forces: {};\n".format(len(App.ActiveDocument.Forces.getSubObjects())))
            if hasattr(App.ActiveDocument, "gravity"):
                f.write("        gravity;\n")
            f.write("end: control data;\n\n")

            f.write("begin: nodes;\n")
            for nodeobj in App.ActiveDocument.Nodes.getSubObjects():
                f.write(App.ActiveDocument.getObject(nodeobj[0:-1]).Proxy.writeNode())      # App.ActiveDocument.getObject(nodeobj[0:-1]).Proxy.writeNode()
            f.write("end: nodes;\n\n")

            f.write("begin: elements;\n")
            for bodyobj in App.ActiveDocument.Bodies.getSubObjects():
                f.write(App.ActiveDocument.getObject(bodyobj[0:-1]).Proxy.writeBody())
            f.write("\n")
            for jointobj in App.ActiveDocument.Joints.getSubObjects():
                f.write(App.ActiveDocument.getObject(jointobj[0:-1]).Proxy.writeJoint())
            f.write("\n")
            for forceobj in App.ActiveDocument.Forces.getSubObjects():
                f.write(App.ActiveDocument.getObject(forceobj[0:-1]).Proxy.writeForce())
            f.write("\n")
            if hasattr(App.ActiveDocument, "gravity"):
                f.write(App.ActiveDocument.gravity.Proxy.writeGravity())
            f.write("end: elements;\n\n")
        else:
            App.Console.PrintMessage("MBDyn model does not exist")

def check_solid(sol_obj):
    '''checks if FreeCAD odject is solid'''
    if hasattr(sol_obj, 'Shape'):
        App.Console.PrintMessage(" checksolid: " + sol_obj.Name + "\n")
        if sol_obj.Shape.ShapeType == 'Solid' or sol_obj.Shape.ShapeType == 'Compound':
            return True
        else:
            return False
    else:
        return False


def calc_placement(pos, orient, orient_des):
    '''calculate FreeCAD placement from MBDyn position and orientation matrix'''
    tu = App.Units.parseQuantity
    m = App.Matrix()
    x_vec = App.Vector(0,0,0)
    y_vec = App.Vector(0,0,0)
    z_vec = App.Vector(0,0,0)
    if orient_des == 'xy' or orient_des == 'xz' or orient_des == 'yz':
        if orient_des == 'xy':
            x_vec = orient[0]
            x_vec.normalize()  # just to be sure; it's important to have the matrix normalized
            z_vec = x_vec.cross(orient[1])
            Z_vec.normalize()
            y_vec = z_vec.cross(x_vec)
            y_vec.normalize()
        elif orient_des == 'xz':
            z_vec = orient[2]
            z_vec.normalize()  # just to be sure; it's important to have the matrix normalized
            y_vec = z_vec.cross(orient[0])
            y_vec.normalize()
            x_vec = y_vec.cross(z_vec)
            x_vec.normalize()
        elif orient_des == 'yz':
            y_vec = orient[1]
            y_vec.normalize()  # just to be sure; it's important to have the matrix normalized
            x_vec = y_vec.cross(orient[2])
            x_vec.normalize()
            z_vec = x_vec.cross(y_vec)
            z_vec.normalize()
        # make matrix
        m.A = list(x_vec)+[0.0]+list(y_vec)+[0.0]+list(z_vec)+[0.0]+[0.0]*3+[1.0]
        m.transpose() # local axes vectors are columns of matrix, but we put them in as rwos, because it is convenient, and then transpose it.
        # make placement out of matrix,

    elif orient_des == 'euler123' or orient_des == 'euler321':  # euler angles
        eulers = orient[0]
        m_roll = App.Matrix(); m_pitch = App.Matrix(); m_yaw = App.Matrix()
        m_roll.unity(); m_pitch.unity(); m_yaw.unity();
        if orient_des == 'euler123':
            m_roll.rotate(eulers.x)
            m_pitch.rotate(eulers.y)
            m_yaw.rotate(eulers.z)
            m = m_roll.multiply(m_pitch)
            m = m.multiply(m_yaw)
        if orient_des == 'euler321':
            m_roll.rotate(eulers.z)
            m_pitch.rotate(eulers.y)
            m_yaw.rotate(eulers.x)
            m = m_yaw.multiply(m_pitch)
            m = m.multiply(m_roll)

    pla = App.Placement(m)
    Rot = pla.Rotation
    return App.Placement(pos, Rot)

def find_joint_label():
    maxjointnum = 0
    for jnt in App.ActiveDocument.Joints.Group:
        if maxjointnum < jnt.joint_label:
            maxjointnum = jnt.joint_label
    return maxjointnum + 1

def find_node_label():
    maxnodenum = 0
    App.Console.PrintMessage(" find node: ") # + str(maxnodeum) + "\n")
    for nod in App.ActiveDocument.Nodes.Group:
        if maxnodenum < nod.node_label:
            maxnodenum = nod.node_label
    return maxnodenum + 1

def find_body_label():
    maxbodynum = 0
    for bod in App.ActiveDocument.Bodies.Group:
        if maxbodynum < bod.label:
            maxbodynum = bod.label
    return maxbodynum + 1

def find_drive_label():
    maxdrivenum = 0
    App.Console.PrintMessage(" find drive: ")
    for drive in App.ActiveDocument.Drive_callers.Group:
        if maxdrivenum < drive.label:
            maxdrivenum = drive.label
    return maxdrivenum + 1

'''
    Rot.A11 = tu('cos('+str(orient.x)+')*cos('+str(orient.y)+')')
    Rot.A12 = tu('cos('+str(orient.x)+')*sin('+str(orient.y)+')*sin('+str(orient.z)+')-sin('+str(orient.x)+')*cos('+str(orient.z)+')')
    Rot.A13 = tu('cos('+str(orient.x)+')*sin('+str(orient.y)+')*cos('+str(orient.z)+')+sin('+str(orient.x)+')*sin('+str(orient.z)+')')
    Rot.A14 = pos.x
    Rot.A21 = tu('sin('+str(orient.x)+')*cos('+str(orient.y)+')')
    Rot.A22 = tu('sin('+str(orient.x)+')*sin('+str(orient.y)+')*sin('+str(orient.z)+')+cos('+str(orient.x)+')*cos('+str(orient.z)+')')
    Rot.A23 = tu('sin('+str(orient.x)+')*sin('+str(orient.y)+')*cos('+str(orient.z)+')-cos('+str(orient.x)+')*sin('+str(orient.z)+')')
    Rot.A24 = pos.y
    Rot.A31 = tu('-sin('+str(orient.y)+')')
    Rot.A32 = tu('cos('+str(orient.y)+')*sin('+str(orient.z)+')')
    Rot.A33 = tu('cos('+str(orient.y)+')*sin('+str(orient.z)+')')
    Rot.A34 = pos.z
    Rot.A41 = 0.0; Rot.A42 = 0.0; Rot.A43 = 0.0; Rot.A44 = 1.0;
    pl = App.Placement(Rot)
    return pl
'''
