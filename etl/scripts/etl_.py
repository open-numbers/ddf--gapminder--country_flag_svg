# -*- coding: utf-8 -*-

import os
import pandas as pd
import xmlformatter


source_dir = '../source/ddf--open_numbers'
formatter = xmlformatter.Formatter(compress=True)


def minify_svg_file(code):
    path = os.path.join('../source/minify_svg', f'{code}.svg')
    with open(path, 'r') as f:
        content = f.read()
        res = formatter.format_string(content).decode('utf8')
    return res.replace('\n', '')


def main():
    country_df = pd.read_csv(os.path.join(source_dir, 'ddf--entities--geo--country.csv'),
                             keep_default_na=False, na_values=[''], dtype=str)
    country_df = country_df[['country', 'iso3166_1_alpha2']].set_index('country')
    country_df['flag_svg'] = country_df['iso3166_1_alpha2'].map(lambda x: minify_svg_file(x) if not pd.isnull(x) else x)
    country_df['flag_svg'].to_csv('../../ddf--entities--geo--country.csv')

    geo_df = pd.read_csv(os.path.join(source_dir, 'ddf--entities--geo.csv'),
                         keep_default_na=False, na_values=[''], dtype=str)
    geo_df = geo_df[['geo', 'iso3166_1_alpha2']].set_index('geo')
    geo_df['flag_svg'] = geo_df['iso3166_1_alpha2'].map(lambda x: minify_svg_file(x) if not pd.isnull(x) else x)
    geo_df['flag_svg'].to_csv('../../ddf--entities--geo.csv')

    print('done.')


if __name__ == '__main__':
    main()
