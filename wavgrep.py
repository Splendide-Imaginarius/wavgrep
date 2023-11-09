from pathlib import Path
import subprocess

from tqdm import tqdm

import crosslooper

__version__ = "1.0.1"
__author__ = """Splendide Imaginarius"""

def cli_parser(**ka):
    parser = crosslooper.cli_parser(**ka)

    parser.description = wavgrep.__doc__

    if 'in-file' not in ka:
        parser.add_argument(
            'in-file',
            action='store',
            type=str,
            help='Audio file to search for.')
    if 'in-dir' not in ka:
        parser.add_argument(
            '--in-dir',
            dest='in-dir',
            action='store',
            default='.',
            type=str,
            help='Directory containing audio files to search. ' +
                 '(default: working directory')
    if 'start' not in ka:
        parser.add_argument(
            '--start',
            dest='start',
            action='store',
            default=15.0,
            type=float,
            help='Start position (seconds) of input file to compare. ' +
                 '(default: 15)')
    if 'len' not in ka:
        parser.add_argument(
            '--len',
            dest='len',
            action='store',
            default=15.0,
            type=float,
            help='Length (seconds) of input file to compare. ' +
                 '(default: 15)')
    if 'count' not in ka:
        parser.add_argument(
            '--count',
            dest='count',
            action='store',
            default=10,
            type=int,
            help='Number of top matches to display. ' +
                 '(default: 10; use 0 for all matches)')

    return parser

def wavgrep(**ka):
    """CLI interface to find an audio file containing similar content.
    ffmpeg needs to be available.
    """

    ka['in1'] = None
    ka['in2'] = None
    ka['show'] = False
    ka['loop-start-min'] = None
    ka['loop-search-len'] = None
    ka['verbose'] = False
    ka['loop'] = False
    ka['loop-start-max'] = None
    ka['loop-end-min'] = None
    ka['loop-len-min'] = None
    ka['loop-search-step'] = None
    ka['loop-force'] = False
    ka['loop-enable-seconds-tags'] = False
    ka['samples'] = False
    ka['skip'] = False

    parser = cli_parser(**ka)
    args = parser.parse_args().__dict__
    ka.update(args)

    ka['in1'] = ka['in-file']
    ka['loop-start-min'] = ka['start']
    ka['loop-search-len'] = ka['len']

    in_file_path = Path(ka['in-file'])
    if not in_file_path.exists():
        raise Exception(f'{in_file_path} does not exist')

    p = Path(ka['in-dir'])

    corrs = {}

    files = list(p.rglob('*'))

    pbar = ka['pbar'] if 'pbar' in ka else tqdm(unit='track')
    pbar.set_description(f"Correlating {in_file_path.name}")
    pbar.reset(total=len(files))

    for f in files:
        ka['in2'] = f.resolve()
        try:
            _, _, ca = crosslooper.file_offset(use_argparse=False, **ka)
        except subprocess.CalledProcessError:
            # ffmpeg couldn't read the file, so it's probably not a legit audio file.
            pbar.update()
            continue
        corrs[f.name] = ca
        pbar.update()
    pbar.close()

    print('')

    top = sorted(corrs, key=corrs.get, reverse=True)
    if ka['count'] != 0 and ka['count'] < len(top):
        top = top[:ka['count']]

    print('WavGrep Results:')
    for f in top:
        print(int(corrs[f]), f)

main = wavgrep
if __name__ == '__main__':
    main()
