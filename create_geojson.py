import json

features = []

h_minor_spacing = 0.002
v_minor_spacing = 0.0004
v_major_spacing = 0.002
sq_size = 0.001


for k in range(2):
	x_translate = 5*(sq_size+h_minor_spacing)+3*sq_size
	for j in range(6):
		for i in range(5):

			workstation_index_start = 10+70*(1-k)+1

			workstation_name_base = "00"+str(workstation_index_start+i+10*j)
			workstation_name = "R"+workstation_name_base[len(workstation_name_base)-3:]
			workstation = {
			  "type": "Feature",
			  "properties": {
			    "workstation": workstation_name
			  },
			  "geometry": {
			    "type": "Polygon",
			    "coordinates": [
			      [
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing)),6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size)+sq_size,6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing)),6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size)+sq_size,6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+sq_size,6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+sq_size,6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing)),6)
			        ]
			      ]
			    ]
			  }
			}
			features.append(workstation)

		horizontal_bar = {
		  "type": "Feature",
		  "properties": {},
		  "geometry": {
		    "type": "Polygon",
		    "coordinates": [
		      [
		        [
		          round((k*x_translate),6),
		          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+(v_minor_spacing+sq_size),6)
		        ],
		        [
		          round((k*x_translate)+5*(h_minor_spacing+sq_size),6),
		          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+(v_minor_spacing+sq_size),6)
		        ],
		        [
		          round((k*x_translate)+5*(h_minor_spacing+sq_size),6),
		          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+(v_minor_spacing+sq_size)+sq_size,6)
		        ],
		        [
		          round((k*x_translate),6),
		          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+(v_minor_spacing+sq_size)+sq_size,6)
		        ],
		        [
		          round((k*x_translate),6),
		          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+(v_minor_spacing+sq_size),6)
		        ]
		      ]
		    ]
		  }
		}
		features.append(horizontal_bar)

		for i in range(5):
			workstation_name_base = "00"+str(workstation_index_start+i+5+10*j)
			workstation_name = "R"+workstation_name_base[len(workstation_name_base)-3:]
			workstation = {
			  "type": "Feature",
			  "properties": {
			    "workstation": workstation_name
			  },
			  "geometry": {
			    "type": "Polygon",
			    "coordinates": [
			      [
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+2*(v_minor_spacing+sq_size),6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size)+sq_size,6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+2*(v_minor_spacing+sq_size),6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size)+sq_size,6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+2*(v_minor_spacing+sq_size)+sq_size,6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+2*(v_minor_spacing+sq_size)+sq_size,6)
			        ],
			        [
			          round((k*(x_translate+h_minor_spacing))+i*(h_minor_spacing+sq_size),6),
			          round((j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+2*(v_minor_spacing+sq_size),6)
			        ]
			      ]
			    ]
			  }
			}
			features.append(workstation)

vertical_bar = {
  "type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          round(5*(sq_size+h_minor_spacing)+sq_size,6),
          round(sq_size+v_minor_spacing,6)
        ],
        [
          round(5*(sq_size+h_minor_spacing)+sq_size+sq_size,6),
          round(sq_size+v_minor_spacing,6)
        ],
        [
          round(5*(sq_size+h_minor_spacing)+sq_size+sq_size,6),
          round((sq_size+v_minor_spacing)+(j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+sq_size,6)
        ],
        [
          round(5*(sq_size+h_minor_spacing)+sq_size,6),
          round((sq_size+v_minor_spacing)+(j*(3*sq_size+2*v_minor_spacing+v_major_spacing))+sq_size,6)
        ],
        [
          round(5*(sq_size+h_minor_spacing)+sq_size,6),
          round(sq_size+v_minor_spacing,6)
        ]
      ]
    ]
  }
}
features.append(vertical_bar)

geojson_object = {
  "type": "FeatureCollection",
  "features": features
}

print(json.dumps(geojson_object))