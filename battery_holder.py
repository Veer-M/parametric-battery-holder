import argparse
import math
from pathlib import Path
from build123d import BuildPart, BuildSketch, Rectangle, Circle, Locations, Mode, extrude, export_step, export_stl

def dimensions(series=4, parallel=2, diameter=18.5, pitch=19.5, wall=2.0):
    if not isinstance(series,int) or not isinstance(parallel,int) or series < 1 or parallel < 1:
        raise ValueError('Series and parallel counts must be positive integers')
    if not all(math.isfinite(v) and v > 0 for v in (diameter,pitch,wall)) or pitch <= diameter:
        raise ValueError('Dimensions must be positive and pitch must exceed diameter')
    return ((parallel-1)*pitch+diameter+2*wall, (series-1)*pitch+diameter+2*wall)

def build_holder(series=4, parallel=2, diameter=18.5, height=65.5, pitch=19.5, wall=2.0):
    width, depth = dimensions(series,parallel,diameter,pitch,wall)
    if not math.isfinite(height) or height <= 0:
        raise ValueError('Height must be positive and finite')
    with BuildPart() as holder:
        with BuildSketch():
            Rectangle(width,depth)
            for row in range(series):
                for column in range(parallel):
                    x = (column-(parallel-1)/2)*pitch
                    y = (row-(series-1)/2)*pitch
                    with Locations((x,y)):
                        Circle(diameter/2,mode=Mode.SUBTRACT)
        extrude(amount=height)
    return holder.part

def main():
    parser = argparse.ArgumentParser(description='Generate a battery cell holder CAD model')
    parser.add_argument('--series',type=int,default=4)
    parser.add_argument('--parallel',type=int,default=2)
    parser.add_argument('--diameter',type=float,default=18.5)
    parser.add_argument('--height',type=float,default=65.5)
    parser.add_argument('--pitch',type=float,default=19.5)
    parser.add_argument('--wall',type=float,default=2)
    parser.add_argument('--output',default='battery_holder.step')
    args = parser.parse_args()
    try:
        part = build_holder(args.series,args.parallel,args.diameter,args.height,args.pitch,args.wall)
    except ValueError as error:
        parser.error(str(error))
    suffix = Path(args.output).suffix.lower()
    if suffix in ('.step','.stp'):
        success = export_step(part,args.output)
    elif suffix == '.stl':
        success = export_stl(part,args.output)
    else:
        parser.error('Output must end in .step, .stp, or .stl')
    if not success:
        raise OSError(f'Export failed: {args.output}')
    print(f'Wrote {args.output}; solid volume {part.volume:.2f} mm^3')

if __name__ == '__main__':
    main()
