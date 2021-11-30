# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysaito <ysaito@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/27 21:17:56 by ysaito            #+#    #+#              #
#    Updated: 2021/11/30 23:16:45 by ysaito           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM    debian:buster

RUN     apt-get update && apt-get -y upgrade \
        && apt-get -y install \
            fcgiwrap \
            nginx \
            vim
# fcgiwrap
RUN     cp /usr/share/doc/fcgiwrap/examples/nginx.conf /etc/nginx/fcgiwrap.conf \
        && mkdir -p /usr/lib/cgi-bin/
COPY    ./srcs/cgi/bash.cgi /usr/lib/cgi-bin/bash.cgi
COPY    ./srcs/cgi/sh.cgi /usr/lib/cgi-bin/sh.cgi
RUN     chmod -R 755 /usr/lib/cgi-bin/

# HTML file
COPY    ./srcs/html/ /var/www/html/

# nginx config
COPY    ./srcs/sites-available/default /etc/nginx/sites-available/default

# run.sh
COPY    ./srcs/run.sh /tmp/run.sh
RUN     chmod 755 /tmp/run.sh

#CMD     ["/usr/sbin/nginx", "-g", "daemon off;"]

CMD     ["bash", "/tmp/run.sh"]