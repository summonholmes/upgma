"""
This file demonstrates how to construct a distance matrix.

All sequences were retrieved from an ncbi protein search for
'sonic hedgehog'.
"""
# Red Junglefowl
Shh_Gallus_gallus = "MVEMLLLTRILLVGFICALLVSSGLTCGPGRGIGKRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKIT" \
    "RNSERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNALAISVMNQWPGVKLRVTEGWDEDGHHSEE" \
    "SLHYEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSATVHL" \
    "EHGGTKLVKDLSPGDRVLAADADGRLLYSDFLTFLDRMDSSRKLFYVIETRQPRARLLLTAAHLLFVAPQ" \
    "HNQSEATGSTSGQALFASNVKPGQRVYVLGEGGQQLLPASVHSVSLREEASGAYAPLTAQGTILINRVLA" \
    "SCYAVIEEHSWAHWAFAPFRLAQGLLAALCPDGAIPTAATTTTGIHWYSRLLYRIGSWVLDGDALHPLGM" \
    "VAPAS"

# Zebrafish
Shh_Danio_rerio = "MRLLTRVLLVSLLTLSLVVSGLACGPGRGYGRRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKITRNS" \
    "ERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNSLAISVMNHWPGVKLRVTEGWDEDGHHFEESLH" \
    "YEGRAVDITTSDRDKSKYGTLSRLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSALVSLQDG" \
    "GQKAVKDLNPGDKVLAADSAGNLVFSDFIMFTDRDSTTRRVFYVIETQEPVEKITLTAAHLLFVLDNSTE" \
    "DLHTMTAAYASSVRAGQKVMVVDDSGQLKSVIVQRIYTEEQRGSFAPVTAHGTIVVDRILASCYAVIEDQ" \
    "GLAHLAFAPARLYYYVSSFLFPQNSSSRSNATLQQEGVHWYSRLLYQMGTWLLDSNMLHPLGMSVNSS"

# Indonesian Coelacanth
Shh_Latimeria_menadoensis = "MDEMLLLTRIVLVGLICSSLVSSGLTCGPGRGYGRRKYPKKLTPLAYKQFIPNVAEKTLGASGRYEGKIT" \
    "RNSERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNSLAISVMNQWPGVKLRVTEGWDEDGHHSEE" \
    "SLHYEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGLATVTL" \
    "EDGGTKFVKDLSPGDRVLAADDQGKLVYSDFLMFLDKEEESQKVFYVIETKEPLKRITLTAAHLLFVAQN" \
    "SSDNLSPFKATFASEIKPGQIIFVAHGDDTHLMAATVERVVLEEDTGAYAPLTNQGTILINRVWASCYAV" \
    "IEQHKWAHWAFAPVRMGYVISSLFFPKDILKYNGTFQENGVHWYSKTLYQIGTWVLDNDYIHPLGMPERS" \
    "S"

# Olive Flounder
Shh_Paralichthys_olivaceus = "MLLWTRIVLAGVICLSLVSSGMGCGPGRGYGRRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKITRNS" \
    "ERFKELTPNYNTDIIFKDEENTGADRLMTQRCKDKLNSLAISVMNQWPGVKLRVTEGWDEDGHHFEESLH" \
    "YEGRAVDITTSDRDKSKYGTLSRLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSSTVTLQDG" \
    "TKKPVKALQTGDRVLAADAHGQPVYTDFIMFIDQDSTTRRLFYVIETDSGQKITLTAAHLLFVGHSNSTE" \
    "RAHRGMSAVFASQVRPGQTVFVLDAERLQPVTVKRIYTQEHEGSFAPVTAQGTVVVDQVLASCYAVIQDH" \
    "ELAHWALAPVRLAHWVSSLLFSSQPQASAQKDGVHWYSKILYQLGTWLLDSHSIHPLGMSVYPS"

# Carp
Shh_Cyprinus_carpio = "MRLMTRVLLVSLLSLSLVVSGLACGPGRGYGRRKHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKITRNS" \
    "ERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDRLNSLAISVMNQWPGVKLRVTEGWDEDGHHFEESLH" \
    "YEGRAVDITTSDRDKSKYGTLSRLAVEAGFDWVYYGSKAHIHCSVKAENSVAAKSGGCFPGSALVALKDG" \
    "RQKAVKDLNPGDKVLAADGNGKLVYSDFIMFTDRDSATRRVFYVIETKEPVEKITLTAAHLLFVLDNSTD" \
    "DLHSMTAAFASSVRAGQKVMVVDDSGPLKSVIVERIYTEEHQGSFAPVTAHGTIVVDRILASCYAVIEDH" \
    "SLAHLAFAPVRLYYDVSSVLFPKNFISQSNATLQQEGVHWYSKLLFQIGAWLLDSRMLHPLGMSVNSS"

# Little Skate
Shh_Leucoraja_erinacea = "MMLTRIVLVGLVCCSLFSSARACGPGRGYGRRKHPRKLTPLAYKQFIPNVAEKTLGASGRYEGKITRNSE" \
    "RFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNSLAISVMNQWPGVKLRVTEGWDEDGHHSEESLHY" \
    "EGRAVDITTSDRDRSKYGMLARLAVEAGFDWVNYESKAHIHCSVKAENSVAAKSGGCFPASARVSLENGD" \
    "TKQVKDLTPGDRVLAADERGNLLYSDFVMFLDRAEEVEKVFYVVETREPRRKLALTAAHLLFVGHATNDG" \
    "QLGLKATFASKVRSGQLVYITDGDSHRLRPARVDKVYLEEMIGAYAPLTIQGTVVIDQVLTSCYAVIEEH" \
    "SLAHWAFAPVRMRYTARSLLLPSDPPAVNCTVQAGGVHWYSSALYQIGRWVLNGASIHPLGMALDSS"

# Mouse
Shh_Mus_musculus = "MLLLLARCFLVILASSLLVCPGLACGPGRGFGKRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKITRN" \
    "SERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNALAISVMNQWPGVKLRVTEGWDEDGHHSEESL" \
    "HYEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSATVHLEQ" \
    "GGTKLVKDLRPGDRVLAADDQGRLLYSDFLTFLDRDEGAKKVFYVIETLEPRERLLLTAAHLLFVAPHND" \
    "SGPTPGPSALFASRVRPGQRVYVVAERGGDRRLLPAAVHSVTLREEEAGAYAPLTAHGTILINRVLASCY" \
    "AVIEEHSWAHRAFAPFRLAHALLAALAPARTDGGGGGSIPAAQSATEARGAEPTAGIHWYSQLLYHIGTW" \
    "LLDSETMHPLGMAVKSS"

# Chimpanzee
Shh_Pan_troglodytes = "MGEMLLLARCLLLVLVSSLLVCSGLACGPGRGFGKRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKIS" \
    "RNSERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNALAISVMNQWPGVKLRVTEGWDEDGHHSEE" \
    "SLHYEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSATVHL" \
    "EQGGTKLVKDLSPGDRVLAADDQGRLLYSDFLTFLDRDDGAKKVFYVIETREPRERLLLTAAHLLFVAPH" \
    "NDSATGGPEASSGSGPPSGGALGPRALFASRVRPGQRVYVVAERDGDRRLLPAAVHSVTLSEEAAGAYAP" \
    "LTAQGTILINRVLASCYAVIEEHSWAHRAFAPFRLAHALLAALAPARTDRGGDSGGGDRGGGGGRVALPA" \
    "PGAADAPGAGATAGIHWYSQLLYQIGTWLLDSEALHPLGMAVKSS"

# Human
Shh_Homo_sapiens = "MLLLARCLLLVLVSSLLVCSGLACGPGRGFGKRRHPKKLTPLAYKQFIPNVAEKTLGASGRYEGKISRNS" \
    "ERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDKLNALAISVMNQWPGVKLRVTEGWDEDGHHSEESLH" \
    "YEGRAVDITTSDRDRSKYGMLARLAVEAGFDWVYYESKAHIHCSVKAENSVAAKSGGCFPGSATVHLEQG" \
    "GTKLVKDLSPGDRVLAADDQGRLLYSDFLTFLDRDDGAKKVFYVIETREPRERLLLTAAHLLFVAPHNDS" \
    "ATGEPEASSGSGPPSGGALGPRALFASRVRPGQRVYVVAERDGDRRLLPAAVHSVTLSEEAAGAYAPLTA" \
    "QGTILINRVLASCYAVIEEHSWAHRAFAPFRLAHALLAALAPARTDRGGDSGGGDRGGGGGRVALTAPGA" \
    "ADAPGAGATAGIHWYSQLLYQIGTWLLDSEALHPLGMAVKSS"


def init_pairwise_dist(seq_1, seq_2):
    """
    If a sequence is longer or shorter than another, the difference must be
    used for initialization
    """
    if len(seq_1) > len(seq_2):
        return len(seq_1) - len(seq_2)
    elif len(seq_2) > len(seq_1):
        return len(seq_2) - len(seq_1)
    else:
        return 0


def count_diff(seq_1, seq_2):
    """
    The actual amino acid to amino acid comparison occurs here.
    """
    total_diff = 0
    for char_1, char_2 in zip(seq_1, seq_2):
        if char_1 != char_2:
            total_diff += 1
    return total_diff


"""
A dictionary of pairwise comparisons is constructed using
n factorial to retrieve all relavent combinations.
"""
pairwise_diff = {
    "Red Junglefowl vs. Zebrafish":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Danio_rerio) + count_diff(
        Shh_Gallus_gallus, Shh_Danio_rerio),
    "Red Junglefowl vs. Indonesian Coelacanth":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Latimeria_menadoensis) +
    count_diff(Shh_Gallus_gallus, Shh_Latimeria_menadoensis),
    "Red Junglefowl vs. Olive Flounder":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Paralichthys_olivaceus) +
    count_diff(Shh_Gallus_gallus, Shh_Paralichthys_olivaceus),
    "Red Junglefowl vs. Carp":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Cyprinus_carpio) + count_diff(
        Shh_Gallus_gallus, Shh_Cyprinus_carpio),
    "Red Junglefowl vs. Little Skate":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Leucoraja_erinacea) + count_diff(
        Shh_Gallus_gallus, Shh_Leucoraja_erinacea),
    "Red Junglefowl vs. Mouse":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Mus_musculus) + count_diff(
        Shh_Gallus_gallus, Shh_Mus_musculus),
    "Red Junglefowl vs. Chimpanzee":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Pan_troglodytes) + count_diff(
        Shh_Gallus_gallus, Shh_Pan_troglodytes),
    "Red Junglefowl vs. Human":
    init_pairwise_dist(Shh_Gallus_gallus, Shh_Homo_sapiens) + count_diff(
        Shh_Gallus_gallus, Shh_Homo_sapiens),
    "Zebrafish vs. Indonesian Coelacanth":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Latimeria_menadoensis) +
    count_diff(Shh_Danio_rerio, Shh_Latimeria_menadoensis),
    "Zebrafish vs. Olive Flounder":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Paralichthys_olivaceus) +
    count_diff(Shh_Danio_rerio, Shh_Paralichthys_olivaceus),
    "Zebrafish vs. Carp":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Cyprinus_carpio) + count_diff(
        Shh_Danio_rerio, Shh_Cyprinus_carpio),
    "Zebrafish vs. Little Skate":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Leucoraja_erinacea) + count_diff(
        Shh_Danio_rerio, Shh_Leucoraja_erinacea),
    "Zebrafish vs. Mouse":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Mus_musculus) + count_diff(
        Shh_Danio_rerio, Shh_Mus_musculus),
    "Zebrafish vs. Chimpanzee":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Pan_troglodytes) + count_diff(
        Shh_Danio_rerio, Shh_Pan_troglodytes),
    "Zebrafish vs. Human":
    init_pairwise_dist(Shh_Danio_rerio, Shh_Homo_sapiens) + count_diff(
        Shh_Danio_rerio, Shh_Homo_sapiens),
    "Indonesian Coelacanth vs. Olive Flounder":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Paralichthys_olivaceus) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Paralichthys_olivaceus),
    "Indonesian Coelacanth vs. Carp":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Cyprinus_carpio) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Cyprinus_carpio),
    "Indonesian Coelacanth vs. Little Skate":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Leucoraja_erinacea) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Leucoraja_erinacea),
    "Indonesian Coelacanth vs. Mouse":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Mus_musculus) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Mus_musculus),
    "Indonesian Coelacanth vs. Chimpanzee":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Pan_troglodytes) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Pan_troglodytes),
    "Indonesian Coelacanth vs. Human":
    init_pairwise_dist(Shh_Latimeria_menadoensis, Shh_Homo_sapiens) +
    count_diff(Shh_Latimeria_menadoensis, Shh_Homo_sapiens),
    "Olive Flounder vs. Carp":
    init_pairwise_dist(Shh_Paralichthys_olivaceus, Shh_Cyprinus_carpio) +
    count_diff(Shh_Paralichthys_olivaceus, Shh_Cyprinus_carpio),
    "Olive Flounder vs. Little Skate":
    init_pairwise_dist(Shh_Paralichthys_olivaceus, Shh_Leucoraja_erinacea) +
    count_diff(Shh_Paralichthys_olivaceus, Shh_Leucoraja_erinacea),
    "Olive Flounder vs. Mouse":
    init_pairwise_dist(Shh_Paralichthys_olivaceus, Shh_Mus_musculus) +
    count_diff(Shh_Paralichthys_olivaceus, Shh_Mus_musculus),
    "Olive Flounder vs. Chimpanzee":
    init_pairwise_dist(Shh_Paralichthys_olivaceus, Shh_Pan_troglodytes) +
    count_diff(Shh_Paralichthys_olivaceus, Shh_Pan_troglodytes),
    "Olive Flounder vs. Human":
    init_pairwise_dist(Shh_Paralichthys_olivaceus, Shh_Homo_sapiens) +
    count_diff(Shh_Paralichthys_olivaceus, Shh_Homo_sapiens),
    "Carp vs. Little Skate":
    init_pairwise_dist(Shh_Cyprinus_carpio, Shh_Leucoraja_erinacea) +
    count_diff(Shh_Cyprinus_carpio, Shh_Leucoraja_erinacea),
    "Carp vs. Mouse":
    init_pairwise_dist(Shh_Cyprinus_carpio, Shh_Mus_musculus) + count_diff(
        Shh_Cyprinus_carpio, Shh_Mus_musculus),
    "Carp vs. Chimpanzee":
    init_pairwise_dist(Shh_Cyprinus_carpio, Shh_Pan_troglodytes) + count_diff(
        Shh_Cyprinus_carpio, Shh_Pan_troglodytes),
    "Carp vs. Human":
    init_pairwise_dist(Shh_Cyprinus_carpio, Shh_Homo_sapiens) + count_diff(
        Shh_Cyprinus_carpio, Shh_Homo_sapiens),
    "Little Skate vs. Mouse":
    init_pairwise_dist(Shh_Leucoraja_erinacea, Shh_Mus_musculus) + count_diff(
        Shh_Leucoraja_erinacea, Shh_Mus_musculus),
    "Little Skate vs. Chimpanzee":
    init_pairwise_dist(Shh_Leucoraja_erinacea, Shh_Pan_troglodytes) +
    count_diff(Shh_Leucoraja_erinacea, Shh_Pan_troglodytes),
    "Little Skate vs. Human":
    init_pairwise_dist(Shh_Leucoraja_erinacea, Shh_Homo_sapiens) + count_diff(
        Shh_Leucoraja_erinacea, Shh_Homo_sapiens),
    "Mouse vs. Chimpanzee":
    init_pairwise_dist(Shh_Mus_musculus, Shh_Pan_troglodytes) + count_diff(
        Shh_Mus_musculus, Shh_Pan_troglodytes),
    "Mouse vs. Human":
    init_pairwise_dist(Shh_Mus_musculus, Shh_Homo_sapiens) + count_diff(
        Shh_Mus_musculus, Shh_Homo_sapiens),
    "Chimpanzee vs. Human":
    init_pairwise_dist(Shh_Pan_troglodytes, Shh_Homo_sapiens) + count_diff(
        Shh_Pan_troglodytes, Shh_Homo_sapiens)
}

# Finally, initialize the distance matrix
"""
Use the dictionary above to construct the distance
matrix.  Pairwise comparisons occur both
vertically and horizontally.

Therefore, the distance matrix always possesses redundancy.
However, this is redundancy is required to create a symmetric,
square matrix to work with.

The main diagonal should be all zeros, and the
anti-diagonal should be a palindrome.
"""
sonic_hedgehog = {
    "Red Junglefowl": (0, 403, 174, 406, 403, 398, 411, 197, 430),
    "Zebrafish": (403, 0, 397, 138, 36, 359, 409, 433, 221),
    "Indonesian Coelacanth": (174, 397, 0, 397, 395, 395, 409, 209, 438),
    "Olive Flounder": (406, 138, 397, 0, 139, 343, 407, 443, 241),
    "Carp": (403, 36, 395, 139, 0, 356, 412, 432, 222),
    "Little Skate": (398, 359, 395, 343, 356, 0, 407, 438, 428),
    "Mouse": (411, 409, 409, 407, 412, 407, 0, 434, 426),
    "Chimpanzee": (197, 433, 209, 443, 432, 438, 434, 0, 426),
    "Human": (430, 221, 438, 241, 222, 428, 426, 426, 0)
}
