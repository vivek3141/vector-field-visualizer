import argparse
import take_function as t

parser = argparse.ArgumentParser(description='Run the program')
parser.add_argument('fx', metavar='fx', type=str, help='X Function')
parser.add_argument('fy', metavar='fy', type=str, help='Y Function')
parser.add_argument('--mode', metavar='mode', type=str,
                    help="Specify 'color' or 'black' to choose whether to use actual length or color", default="color",
                    nargs='?')
parser.add_argument('--skip', metavar='skip', type=int, help='Number of units to skip before each vector', default=2,
                    nargs='?')
parser.add_argument('--boundx', metavar='boundx', type=str,
                    help='Number of X values to show. Eg. -10,10', nargs='?', default="-10,10")
parser.add_argument('--boundy', metavar='boundy', type=str, help='Number of X values to show. Eg. -10,10',
                    default='-10,10', nargs='?')
parser.add_argument('--prop', metavar='prop', type=int, help='Set this value to change the cutoff for changing color',
                    default=0, nargs='?')
parser.add_argument('--head_size', metavar='head_size', type=float, help='Size of arrow heads',
                    default=0.5, nargs='?')

args = parser.parse_args()
if args.mode.upper() == "COLOR":
    t = t.graph_color(x_func=args.fx, y_func=args.fy, bound_x=tuple(map(int, args.boundx.split(','))),
                      bound_y=tuple(map(int, args.boundy.split(','))), skip=args.skip, prop=args.prop,
                      head_size=args.head_size)
elif args.mode.upper() == "BLACK":
    t = t.graph(x_func=args.fx, y_func=args.fy, bound_x=tuple(map(int, args.boundx.split(','))),
                bound_y=tuple(map(int, args.boundy.split(','))), skip=args.skip,
                head_size=args.head_size)
