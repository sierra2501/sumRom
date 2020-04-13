import math

def sumRom():

    count = 0
    r = 0

    # 稜線数
    edges_num = xshade.scene().active_shape().number_of_edges

    while count < edges_num:

        if xshade.scene().active_shape().edge(count).active == True:
        
            # 頂点のインデックス値
            edge_v0 = xshade.scene().active_shape().edge(count).v0
            edge_v1 = xshade.scene().active_shape().edge(count).v1

            #  頂点の座標
            vertex_v0 =  xshade.scene().active_shape().vertex(edge_v0).position
            vertex_v1 = xshade.scene().active_shape().vertex(edge_v1).position

            #  長さ
            r = math.sqrt((vertex_v0[0] - vertex_v1[0]) ** 2 + (vertex_v0[1] - vertex_v1[1]) ** 2 + (vertex_v0[2] - vertex_v1[2]) ** 2) + r
    
        else:
            r = 0 + r

        count = count + 1

    return r

def main():

    unit_array = ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"]
    return str(sumRom()) + " " + unit_array[xshade.scene().unit]

result = main()