const safetyData = [
    {
        location: "Financial District",
        boundaries: [
            [37.794, -122.395], [37.794, -122.390], [37.790, -122.390], [37.790, -122.395]
        ],
        safety_index: 15  // Very Safe - Dark Green
    },
    {
        location: "North Beach",
        boundaries: [
            [37.798, -122.405], [37.798, -122.400], [37.795, -122.400], [37.795, -122.405]
        ],
        safety_index: 25  // Safe - Lighter Green
    },
    {
        location: "Chinatown",
        boundaries: [
            [37.792, -122.408], [37.792, -122.403], [37.789, -122.403], [37.789, -122.408]
        ],
        safety_index: 35 // Moderately Safe - Yellowish Green
    },
    {
        location: "Telegraph Hill",
        boundaries: [
            [37.801, -122.409], [37.801, -122.405], [37.798, -122.405], [37.798, -122.409]
        ],
        safety_index: 20 // Safe - Light Green
    },
    {
        location: "Russian Hill",
        boundaries: [
            [37.795, -122.420], [37.795, -122.415], [37.790, -122.415], [37.790, -122.420]
        ],
        safety_index: 35 // Moderately Safe - Yellowish Green
    },
    {
        location: "Marina District",
        boundaries: [
            [37.805, -122.440], [37.805, -122.435], [37.800, -122.435], [37.800, -122.440]
        ],
        safety_index: 30 // Moderately Safe - Green Yellow
    },
    {
        location: "Cow Hollow",
        boundaries: [
            [37.800, -122.440], [37.800, -122.435], [37.795, -122.435], [37.795, -122.440]
        ],
        safety_index: 25 // Safe - Light Green
    },
    {
        location: "Nob Hill",
        boundaries: [
            [37.790, -122.415], [37.790, -122.410], [37.785, -122.410], [37.785, -122.415]
        ],
        safety_index: 40 // Moderate - Light Yellow
    },
    {
        location: "Tenderloin",
        boundaries: [
            [37.785, -122.415], [37.785, -122.410], [37.782, -122.410], [37.782, -122.415]
        ],
        safety_index: 75 // Unsafe - Orange
    },
    {
        location: "Union Square",
        boundaries: [
            [37.787, -122.408], [37.787, -122.403], [37.784, -122.403], [37.784, -122.408]
        ],
        safety_index: 45 // Moderate - Yellow
    },
    {
        location: "Presidio",
        boundaries: [
            [37.800, -122.470], [37.800, -122.465], [37.795, -122.465], [37.795, -122.470]
        ],
        safety_index: 20 // Safe - Light Green
    },
    {
        location: "Golden Gate Park",
        boundaries: [
            [37.770, -122.470], [37.770, -122.465], [37.765, -122.465], [37.765, -122.470]
        ],
        safety_index: 35 // Moderately Safe - Yellowish Green
    },
    {
        location: "Pacific Heights",
        boundaries: [
            [37.790, -122.440], [37.790, -122.435], [37.785, -122.435], [37.785, -122.440]
        ],
        safety_index: 25 // Safe - Lighter Green
    },
    {
        location: "Western Addition",
        boundaries: [
            [37.780, -122.435], [37.780, -122.430], [37.775, -122.430], [37.775, -122.435]
        ],
        safety_index: 50 // Moderate - Orange Yellow
    },
    {
        location: "Haight-Ashbury",
        boundaries: [
            [37.770, -122.450], [37.770, -122.445], [37.765, -122.445], [37.765, -122.450]
        ],
        safety_index: 50 // Moderate - Orange Yellow
    },
    {
        location: "Richmond District",
        boundaries: [
            [37.780, -122.480], [37.780, -122.475], [37.775, -122.475], [37.775, -122.480]
        ],
        safety_index: 40 // Moderate - Light Yellow
    },
    {
        location: "Mission District",
        boundaries: [
            [37.755, -122.420], [37.755, -122.415], [37.750, -122.415], [37.750, -122.420]
        ],
        safety_index: 45 // Moderate - Yellow
    },
    {
        location: "SoMa (South of Market)",
        boundaries: [
            [37.780, -122.410], [37.780, -122.400], [37.770, -122.400], [37.770, -122.410]
        ],
        safety_index: 55 // Moderate - Orange Yellow
    },
    {
        location: "Potrero Hill",
        boundaries: [
            [37.760, -122.400], [37.760, -122.390], [37.750, -122.390], [37.750, -122.400]
        ],
        safety_index: 30 // Safe - Light Green
    },
    {
        location: "Castro District",
        boundaries: [
            [37.765, -122.435], [37.765, -122.430], [37.760, -122.430], [37.760, -122.435]
        ],
        safety_index: 40 // Moderately Safe - Yellowish Green
    },
    {
        location: "Noe Valley",
        boundaries: [
            [37.750, -122.435], [37.750, -122.430], [37.745, -122.430], [37.745, -122.435]
        ],
        safety_index: 25 // Safe - Light Green
    },
    {
        location: "Bernal Heights",
        boundaries: [
            [37.740, -122.415], [37.740, -122.410], [37.735, -122.410], [37.735, -122.415]
        ],
        safety_index: 35 // Moderately Safe - Yellowish Green
    },
    {
        location: "Dogpatch",
        boundaries: [
            [37.760, -122.390], [37.760, -122.385], [37.755, -122.385], [37.755, -122.390]
        ],
        safety_index: 30 // Safe - Light Green
    },
    {
        location: "Inner Sunset",
        boundaries: [
            [37.760, -122.470], [37.760, -122.465], [37.755, -122.465], [37.755, -122.470]
        ],
        safety_index: 40 // Moderately Safe - Yellowish Green
    },
    {
        location: "Outer Sunset",
        boundaries: [
            [37.750, -122.480], [37.750, -122.475], [37.745, -122.475], [37.745, -122.480]
        ],
        safety_index: 50 // Moderate - Orange Yellow
    },
    {
        location: "Inner Richmond",
        boundaries: [
            [37.770, -122.470], [37.770, -122.465], [37.765, -122.465], [37.765, -122.470]
        ],
        safety_index: 30 // Safe - Light Green
    },
    {
        location: "Outer Richmond",
        boundaries: [
            [37.765, -122.480], [37.765, -122.475], [37.760, -122.475], [37.760, -122.480]
        ],
        safety_index: 35 // Moderately Safe - Yellowish Green
    },
    {
        location: "Bayview",
        boundaries: [
            [37.735, -122.400], [37.735, -122.395], [37.730, -122.395], [37.730, -122.400]
        ],
        safety_index: 60 // Unsafe - Light Orange
    },
    {
        location: "Excelsior",
        boundaries: [
            [37.720, -122.430], [37.720, -122.425], [37.715, -122.425], [37.715, -122.430]
        ],
        safety_index: 50 // Moderate - Orange Yellow
    },
    {
        location: "Visitacion Valley",
        boundaries: [
            [37.715, -122.405], [37.715, -122.400], [37.710, -122.400], [37.710, -122.405]
        ],
        safety_index: 55 // Moderate - Orange Yellow
    },
    {
        location: "Glen Park",
        boundaries: [
            [37.740, -122.435], [37.740, -122.430], [37.735, -122.430], [37.735, -122.435]
        ],
        safety_index: 30 // Safe - Light Green
    }
]
